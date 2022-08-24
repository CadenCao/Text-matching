# -*- coding:utf-8 -*-
# author :Caden Cao time:2021/11/23
# 该文档用于获取url和url对应网络源代码并进行相似度匹配
import URLGet
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Edge
from msedge.selenium_tools import Edge
import re
from gensim import corpora, models, similarities


urls = []  # 生命urls为全局变量

# 使用selenium获取网页源代码
class PSGetBySel:
    def __init__(self, url_list):
        self.url_list = url_list

    def PageGet(self):
        for i in self.url_list:
            try:
                web = Edge(r'D:\Python3.10\msedgedriver.exe')
                web.get(i)
                element = WebDriverWait(web, 5, 0.5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="details-button"]')))
                web.find_element_by_xpath('//*[@id="details-button"]').click()
                web.find_element_by_xpath('//*[@id="proceed-link"]').click()
                Source_page = web.page_source
                pattern2 = re.compile(r'[\u4e00-\u9fa5]+')
                Chinese = pattern2.findall(Source_page)
                if not Chinese:
                    print(i, '无中文')
                    continue
                else:
                    print(i, '中文提取成功')
                web.close()
                yield i, Chinese
            except Exception as e:
                print(i, e)
                web.close()
                continue

# 使用tiidf进行相似度匹配
def TF_IDF(text_list, text_new):
    diction = corpora.Dictionary(text_list)  # 构建词袋
    num_features = len(diction.token2id)  # 词典特征数赋值
    corpus = [diction.doc2bow(test) for test in
              text_list]  # 遍历每个样本文档中所有单词取集合并分配ID;转换成稀疏向量如[(0,1),(1.1),(2,2)...](也即语料库)
    tfidf = models.TfidfModel(corpus)  # 用语料库训练TF-IDF模型(去除高重复单词,对重要单词赋高权重)
    tf_texts = tfidf[corpus]  # 获取模型训练后每个高权重单词的TF-IDF值
    kw_vector = diction.doc2bow(text_new)  # 添加被测试数据
    tf_kw = tfidf[kw_vector]  # 获取模型训练后被测试数据每个高权重单词的TF-IDF值
    # 这个函数是采用余弦相似度方法，使用TFIDF将语料转换成词频表示，并计算出每个文档的相似度
    index = similarities.SparseMatrixSimilarity(tf_texts, num_features)  # 通过TF-IDF对整个语料库进行转换并编入索引,以准备相似性查询
    sim = index.get_similarities(tf_kw)  # 计算被测试文档text_new与每个样本文档(也即text_list中元素)的相似度
    return sim


# 被测试文档与其他文档集最大相似度超过0.6则认为是同一文档
if __name__ == '__main__':
    URLGet.Url_get(0, 1000)
    page = PSGetBySel(urls)
    chinese = page.PageGet()
    # Fir = next(chinese)
    text_fir = []
    url_avi = []
    for p in chinese:
        text_fir.append(next(chinese)[1])
        url_avi.append(next(chinese)[0])
        for j in chinese:
            MAX = max(TF_IDF(text_fir, j[1]))
            if MAX < 0.6:
                text_fir.append(j[1])
                url_avi.append(j[0])
            else:
                continue

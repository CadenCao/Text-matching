# 中文网页相似度匹配  
### 主要流程：  
1.**通过request从fofa爬取所需网络链接（urlget.py）**  
2.**通过selenium模块进行自动化爬取全部网页链接对应网页源代码**  
3.**通过tf-idf进行网页相似度匹配，获取独立网页链接**  


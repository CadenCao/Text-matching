import csv
import re
import Agg

# 用于获取fofa网站的网络资产的url
def Url_get(p, q):
    for i in range(p, q):
        import requests

        headers = {
            'authority': 'fofa.so',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://fofa.so/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie': 'Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1638341059,1638510993,1638844776,1638945082; befor_router=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTM0MCwibWlkIjoxMDAwMDM5MjMsInVzZXJuYW1lIjoiYXJtc3Ryb25nNzciLCJleHAiOjE2MzkxNDUyNzAuMjQzNzE4LCJpc3MiOiJyZWZyZXNoIn0.FoG6aoh_fWnSc0rNL86ySNb7F4WcEo6_eJRXQUcTmuCzq70DGLGAtuJvOoviecDvRGVOQmWDDhVqyFkL9ACuLQ; user=%7B%22id%22%3A1340%2C%22mid%22%3A100003923%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22armstrong77%22%2C%22nickname%22%3A%22%22%2C%22email%22%3A%22254428610%40qq.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%22371ec0ab9b4d8b3f8b6cb60f5eb7f9ea%22%2C%22rank_name%22%3A%22%E9%AB%98%E7%BA%A7%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A2%2C%22company_name%22%3A%22%22%2C%22coins%22%3A0%2C%22credits%22%3A8427%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%7D; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1639119649',
            'if-none-match': '"4e969-60T835g+WkynTD9bjgP+JAv3AiI"',
        }

        params = (
            ('qbase64', 'YXBwPSJOZXRTaGFyZS1WUE4i'),
        )

        response = requests.get('https://fofa.so/result', headers=headers, params=params)

        # NB. Original query string below. It seems impossible to parse and
        # reproduce query strings 100% accurately so the one below is given
        # in case the reproduced version is not "correct".
        # response = requests.get('https://fofa.so/result?qbase64=YXBwPSJOZXRTaGFyZS1WUE4i', headers=headers)
        # print(response.text)
        obj = re.compile(
            r'<span class="aSpan"><a href="(.*?)" target="_blank">.*?<i class="iconfont icon-link"></i></a></span>',
            re.S)
        url_gets = obj.finditer(response.text)
        for j in url_gets:
            print(j.group(1))
            # Agg.Urls.append(j.group(1))
            Agg.urls.append(j.group(1))
    # with open(r'C:\Users\11111\Desktop\资产大全\Array-VPN\all_url.csv', 'a', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(urls)


if __name__ == "__main__":

    urls = []
    Url_get(0, 475)
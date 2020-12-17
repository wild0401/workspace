# 抓取Medium.com的文章資料
import urllib.request as req
url="https://medium.com/_/api/home-feed"
# 建立一個Request 物件，附加 Request Headers 的資訊
request=req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")    #根據觀察，取得的資料是json格式
# print(data)
# 解析原始碼，取得每篇文章的標題
import json
data=data.replace("])}while(l);</x>","")
data=json.loads(data)   #把原始的資料解析成字典/列表的表示形式
# print(data)
# 取得 json資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])
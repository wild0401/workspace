# 抓取 PTT 八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    # 建立一個Request 物件，附加 Request Headers 的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    # 解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    # print(root.title.string)
    # titles=root.find("div",class_="title")  #尋找 class="title"的div標籤
    # print(titles.a.string)
    titles=root.find_all("div",class_="title")  #尋找 class="title"的div標籤
    for title in titles:
        if title.a != None: #如果標題包含a標籤(沒有被刪除)，印出來
            print(title.a.string)
    #抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁") #找到內文是"‹ 上頁"的a標籤
    return nextLink["href"]
    
# 主程序: 抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    getData(pageURL)
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
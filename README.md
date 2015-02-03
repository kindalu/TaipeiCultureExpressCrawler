# TaipeiCultureExpressCrawler

這個程式碼會抓台北市文化快遞的活動，轉成json格式。結果放在result.json裡。(目前只抓了2014/11/26 - 2015/1/27間發佈的活動)只要跑run.sh (> sh run.sh)就可以執行，主要程式是用scrapy startproject自動產生的，更動的檔只有item.py和mySpider.py，只要看這兩個檔就夠了。

需要安裝的軟體: python 2.7, scrapy, simplejson (後面兩個用pip install就可以安裝好了)


建議學習scrapy的網頁如下：

http://scrapy-chs.readthedocs.org/zh_CN/latest/index.html (官網的中文化)

http://www.slideshare.net/ErinShellman/downloading-the-internet-with-python-scrapy

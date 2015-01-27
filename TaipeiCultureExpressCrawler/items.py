# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EventItem(scrapy.Item):
    # define the fields for your item here like:

    #crawler抓的網址
    origin_url = scrapy.Field()

    #print response.css('div[class=content] h3 ::text')[0].extract().encode("utf-8")
    title = scrapy.Field() #活動名稱

    #print response.css('div[class=content] p#TypeP ::text')[0].extract().encode("utf-8")
    event_type = scrapy.Field() #活動分類

    #print response.css('div[class=content]  div ::text')[4].extract().encode("utf-8")
    publish_time = scrapy.Field() #發佈日期

    #print response.css('div[class=content]  div#vContent')[0].extract().encode("utf-8")
    desc = scrapy.Field() #活動描述

    #print response.css('div[class=content]  ul p')[2].css('::text')[0].extract().encode("utf-8")
    performer = scrapy.Field() #演出單位

    #print response.css('div[class=content]  ul p')[4].css('::text')[0].extract().encode("utf-8")
    event_period = scrapy.Field() #活動區間

    #print response.css('div[class=content]  ul p')[6].css('::text')[0].extract().encode("utf-8")
    event_time = scrapy.Field() #活動場次

    #print response.css('div[class=content]  ul p')[6].css('::text')[1].extract().encode("utf-8")
    event_location = scrapy.Field() #活動地點

    #print response.css('div[class=content]  ul p')[6].css('::text')[2].extract().encode("utf-8")
    event_address = scrapy.Field() #活動地址

    #經緯度
    lat = scrapy.Field() #latitude
    lng = scrapy.Field() #longitude

    #print response.css('div[class=content]  ul p')[9].css('::text')[0].extract().encode("utf-8")
    ticket_price_list = scrapy.Field() #票價

    #print response.css('div[class=content]  ul p')[11].css('::text')[0].extract().encode("utf-8")
    ticket_link = scrapy.Field() #售票網址

    #print response.css('div[class=content]  ul p')[14].css('::text')[0].extract().encode("utf-8")
    contact_name = scrapy.Field() #活動聯絡人

    #print response.css('div[class=content]  ul p')[16].css('::text')[0].extract().encode("utf-8")
    contact_phone_num = scrapy.Field() #活動電話

    #print response.css('div[class=content]  ul p')[18].css('::text')[0].extract().encode("utf-8")
    contact_fax = scrapy.Field() #活動傳真

    #print response.css('div[class=content]  ul p')[21].css('::text')[0].extract().encode("utf-8")
    event_link = scrapy.Field() #活動網址
    #youtube = scrapy.Field() #youtube
    pass

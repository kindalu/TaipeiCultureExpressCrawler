# -*- coding: utf-8 -*-
import scrapy
import json
import codecs
import urllib
import simplejson
from TaipeiCultureExpressCrawler.items import EventItem

class mySpider(scrapy.Spider):
    name = "culture_express_event"

    #get_coordinates function code from
    #http://stackoverflow.com/questions/15285691/googlemaps-api-address-to-coordinates-latitude-longitude
    def get_coordinates(self, query, from_sensor=False):
        googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
        params = {
            'address': query,
            'sensor': "true" if from_sensor else "false"
        }
        url = googleGeocodeUrl + urllib.urlencode(params)
        json_response = urllib.urlopen(url)
        response = simplejson.loads(json_response.read())
        if response['results']:
            location = response['results'][0]['geometry']['location']
            latitude, longitude = location['lat'], location['lng']
        else:
            latitude, longitude = None, None
        return latitude, longitude

    #define how to generate request
    def start_requests(self):
        url_prefix = "http://cultureexpress.taipei/ViewEvent.aspx?id="
        for event_num in range(2999, 3000):
            url = url_prefix + str(event_num)
            yield scrapy.Request(url, self.parse)

    #parse the respone from generated request
    def parse(self, response):
        if( response.css('div[class=content]') == [] ):
            return 0

        item = EventItem()

        item['origin_url'] = response.url

        item['title'] = response.css('div[class=content] h3 ::text')[0].extract().encode("utf-8")

        item['event_type'] = response.css('div[class=content] p#TypeP ::text')[0].extract().encode("utf-8").split("：")[1]

        item['publish_time'] = response.css('div[class=content]  div ::text')[4].extract().encode("utf-8").split(" ")[1]

        raw_content = response.css('div[class=content]  div#vContent ::text')
        content = ''
        for r in raw_content:
            content = content +" "+ r.extract().encode("utf-8")
        item['desc'] = content

        item['performer'] = response.css('div[class=content]  ul p')[2].css('::text')[0].extract().encode("utf-8")

        item['event_period'] = response.css('div[class=content]  ul p')[4].css('::text')[0].extract().encode("utf-8")

        item['event_time'] = response.css('div[class=content]  ul p')[6].css('::text')[0].extract().encode("utf-8").split("：")[1]

        item['event_location'] = response.css('div[class=content] ul p')[6].css('::text')[1].extract().encode("utf-8").split("：")[1]
        item['event_address'] = response.css('div[class=content] ul p')[6].css('::text')[2].extract().encode("utf-8").split("：")[1]

        latlng = self.get_coordinates(item['event_address'])
        item['lat'] = latlng[0]
        item['lng'] = latlng[1]

        ticket_price_line = response.css('div[class=content]  ul p')[9].css('::text')[0].extract().encode("utf-8")
        if(ticket_price_line.find("是") != -1):
            item['ticket_price_list'] = 0
        else:
            item['ticket_price_list'] = ticket_price_line.split("： ")[1].split("元")[0]

        if(response.css('div[class=content]  ul p')[11].css('::text') != [] ):
            item['ticket_link'] = response.css('div[class=content]  ul p')[11].css('::text')[0].extract().encode("utf-8")
        else:
            item['ticket_link'] = ''

        if(response.css('div[class=content]  ul p')[14].css('::text') != [] ):
            item['contact_name'] = response.css('div[class=content]  ul p')[14].css('::text')[0].extract().encode("utf-8")
        else:
            item['contact_name'] = ''

        if(response.css('div[class=content]  ul p')[16].css('::text') != [] ):
            item['contact_phone_num'] = response.css('div[class=content]  ul p')[16].css('::text')[0].extract().encode("utf-8")
        else:
            item['contact_phone_num'] = ''

        if(response.css('div[class=content]  ul p')[18].css('::text') != [] ):
            item['contact_fax'] = response.css('div[class=content]  ul p')[18].css('::text')[0].extract().encode("utf-8")
        else:
            item['contact_fax'] = ''

        if(response.css('div[class=content]  ul p')[21].css('::text') != [] ):
            item['event_link'] = response.css('div[class=content]  ul p')[21].css('::text')[0].extract().encode("utf-8")
        else:
            item['event_link'] = ''

        with codecs.open('out.json', 'wa') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#            print line
            f.write(line)


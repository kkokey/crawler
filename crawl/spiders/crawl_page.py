# -*- coding: utf-8 -*-
import os
import scrapy
import sys
import unicodedata
import codecs
import json
from datetime import datetime
sys.path.append(os.path.abspath("./"))
from makeFolder import *

reload(sys)
sys.setdefaultencoding('utf-8')

class CrawlPageSpider(scrapy.Spider):
		name = "crawl_page"
		def start_requests(self):
			allowed_domains = ["coupang.com/np/categories/118142"]
			start_urls = ['http://www.coupang.com/np/categories/118142/']
			yield scrapy.Request(start_urls[0], self.parse)

		def parse(self, response):
				
			todayDate = datetime.today()
			itemList = {}
			i = 0

			for product in response.css('ul.baby-product-list dl.baby-product-wrap'):
				name = product.css('dd.name::text').extract()
				price = product.css('strong.price-value::text').extract()
				uStr = unicodedata.normalize('NFKD', name[0])

				item = {}
				item['p-name'] = uStr
				item['p-price'] = price[0]

				itemList[i] = item

				i = i + 1

			# make file
			dirname = "data/coupang"
			makeFolder(dirname)

			jsonOut = json.dumps(itemList, sort_keys=True, indent=2, ensure_ascii=False)
			jsonOut = jsonOut.replace('\\n                    ','')
			jsonOut = jsonOut.replace('\\n                ','')
			self.file = codecs.open(dirname+'/page_'+str(todayDate)+'.json', 'w', encoding='utf-8')
			line = jsonOut + "\n"
			self.file.write(line)
			self.file.close()




# -*- coding: utf-8 -*-
import os
import scrapy
import sys
import unicodedata
import codecs
import json
from datetime import datetime
from makeFolder import *
from db_conn import *

sys.path.append(os.path.abspath("./"))
reload(sys)
sys.setdefaultencoding('utf-8')

class CrawlPageSpider(scrapy.Spider):
		name = "crawl_page"
		
		def start_requests(self):
			allowed_domains = ["coupang.com/np/categories/118142"]
			start_urls = ['http://www.coupang.com/np/categories/118142/']
			yield scrapy.Request(start_urls[0], self.parse)

		def dataToJsonFile(self, rowData):
			dirname = "data/coupang"
			todayDate = datetime.today()
			makeFolder(dirname)

			jsonOut = json.dumps(rowData, sort_keys=True, indent=2, ensure_ascii=False)
			jsonOut = jsonOut.replace('\\n                    ','')
			jsonOut = jsonOut.replace('\\n                ','')
			jsonObj = json.loads(jsonOut)
			self.file = codecs.open(dirname+'/page_'+str(todayDate)+'.json', 'w', encoding='utf-8')
			line = jsonOut + "\n"
			self.file.write(line)
			self.file.close()
			print(jsonObj['0']['p-name'])

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

			### make file
			self.dataToJsonFile(itemList)

			print("### connect database")
			dbConn = dbConnection(self)
			dbConfig = dbConn.getConfig()
			cnx = dbConn.getDbPool(dbConfig)
			dbConn.selectQuery(cnx, "")
			dbConn.close(cnx)
			print("### disconnect database")
	



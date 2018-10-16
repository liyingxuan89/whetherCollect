#!/bin/env python

import urllib
import urllib2
import sys
import os
from lxml import etree
import pandas as pd
import numpy as np

def parser(html):

	content = etree.HTML(html)	
	pattern = '//div[@class="observation-table"]'

	head = pattern + "//thead"
	body = pattern + "//tbody"
	
	data = content.xpath(head) 
	
	if data:
		return data[0].xpath('string()')

	

class whetherCollect(object):
	
	def __init__(self, city, timeList, parser):
		
		self.city = city
		self.time = timeList
		self.parser = parser
		self.url = "https://www.wunderground.com/history/monthly/cn/" + self.city + "/date/"
		self.headers = {
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
				
		}

	def dataSaver(self, savePath):

		data = 0

		with open(savePath, 'w') as f:
			f.write(data)


	def download(self):
		
		for year in self.time:
			realUrls = [self.url + str(year) + "-" + str(x) for x in range(1,2)]
			for url in realUrls:
				request = urllib2.Request(url, headers=self.headers)	
				response = urllib2.urlopen(request)
				html =  response.read()
				data = self.parser(html)
				print data
					

		


def main():
	whether = whetherCollect('chengdu', [2018], parser)
	whether.download()

if __name__ == "__main__":
	main()

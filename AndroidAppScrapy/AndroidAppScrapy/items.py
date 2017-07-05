# -*- coding :  utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in = 
# http ://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AndroidappscrapyItem(scrapy.Item) :
    # define the fields for your item here like: 
    # name = scrapy.Field()
	link = scrapy.Field()
	category = scrapy.Field()
	
	PkgName = scrapy.Field()
	Title = scrapy.Field()
	genre = scrapy.Field()
	score = scrapy.Field()	
	ratingHistogram = scrapy.Field()
	comp = scrapy.Field()
	datePublished = scrapy.Field()
	numDownloads = scrapy.Field()
	ratingValue = scrapy.Field()
	contentRating = scrapy.Field()
	Reviewers = scrapy.Field()
	softwareVersion = scrapy.Field()
	GpCategory = scrapy.Field()
	GpCategory2 = scrapy.Field()
	similarApps = scrapy.Field()
	operatingSystems = scrapy.Field()
	ads = scrapy.Field()
	whatsNew = scrapy.Field()
	inAppMsg = scrapy.Field()
	price = scrapy.Field()
	LogoUrl = scrapy.Field()
	ClkUrl = scrapy.Field()
	mail = scrapy.Field()
	Thumbnails = scrapy.Field() # screenshot
	Desc = scrapy.Field() # description
	Rating = scrapy.Field() #width
	Recommenders = scrapy.Field() #empty in java
	PosId = scrapy.Field() #empty in java
	AppType = scrapy.Field()
	Lan = scrapy.Field()
	Country = scrapy.Field() # set by crawler
	fileSize =  scrapy.Field()# cant find tag due to new version
	genre2 =  scrapy.Field()# cant find tag due to new version
	name = scrapy.Field() # same as title 
	GpTag = scrapy.Field()# cant find tag due to new version
	pass

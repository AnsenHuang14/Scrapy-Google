from AndroidAppScrapy.items import AndroidappscrapyItem
import scrapy
from datetime import datetime

def read_url(path=''):
    start_urls = list()
    with open(path, 'rb') as f:
        start_urls.append(f.read())
    start_urls = start_urls[0].split('\n')
    return start_urls

class App_Spider(scrapy.Spider):
    name = "App_Spider"
    allowed_domains = ["play.google.com"]

    def __init__(self,path, *args,**kwargs):
        super(App_Spider, self).__init__(*args, **kwargs)
        self.start_urls = read_url(path)
        self.date = datetime.now().strftime('%Y%m%d')
        
    def parse(self, response):
        app = AndroidappscrapyItem()

        app['crawlDate'] = self.date

        app['PkgName'] = response.url.split('=')[1].replace('&hl','')
        app['Title'] = response.xpath('//div[@class="id-app-title"]/text()')[0].extract()
        app['genre'] = response.xpath('//span[@itemprop="genre"]/text()')[0].extract()
        app['score'] = response.xpath('//div[@class="score"]/text()')[0].extract()
        
        score_number = list()
        for s in response.xpath('//span[@class="bar-number"]/text()'):
            score_number.append(s.extract().replace(',',''))
        app['ratingHistogram'] = score_number

        app['comp'] = response.xpath('//span[@itemprop="name"]/text()')[0].extract()
        app['datePublished'] = response.xpath('//div[@itemprop="datePublished"]/text()')[0].extract()
        app['numDownloads'] = response.xpath('//div[@itemprop="numDownloads"]/text()')[0].extract()
        app['ratingValue'] =  response.xpath('//div[@class="score"]/text()')[0].extract()
        app['contentRating'] = response.xpath('//div[@itemprop="contentRating"]/text()')[0].extract()
        app['Reviewers'] = response.xpath('//span[@class="reviews-num"]/text()')[0].extract()
        app['softwareVersion'] = response.xpath('//div[@itemprop="softwareVersion"]/text()')[0].extract()
        app['GpCategory'] =  app['genre']
        app['GpCategory2'] = app['genre']

        similar_app = list()
        for s in response.xpath('//span[@class="preview-overlay-container"]//@data-docid'):
            similar_app.append(s.extract())
        app['similarApps'] = similar_app
        
        app['operatingSystems'] = response.xpath('//div[@itemprop="operatingSystems"]/text()')[0].extract().replace(' ','')
        
        if len(response.xpath('//span[@class="ads-supported-label-msg"]/text()'))==0:
            app['ads'] = ''
        else:
            app['ads'] = response.xpath('//span[@class="ads-supported-label-msg"]/text()')[0].extract()
        
        if len(response.xpath('//div[@class="recent-change"]/text()'))==0:
            app['whatsNew'] = ''
        else:
            app['whatsNew'] = response.xpath('//div[@class="recent-change"]/text()')[0].extract()

        if len(response.xpath('//div[@class="inapp-msg"]/text()'))==0:
            app['inAppMsg'] = ''
        else:
            app['inAppMsg'] = response.xpath('//div[@class="inapp-msg"]/text()')[0].extract()
        
        app['price'] =  response.xpath('//meta[@itemprop="price"]//@content')[0].extract()
        app['LogoUrl'] =  response.xpath('//img[@class="cover-image"]//@src')[0].extract()
        app['ClkUrl'] =  response.url
        
        if len(response.xpath('//a[@class="dev-link"]//@href'))==0:
            app['mail'] = ''
        else:
            app['mail'] =  response.xpath('//a[@class="dev-link"]//@href').extract()
        
        app['Thumbnails'] =  response.xpath('//img[@itemprop="screenshot"]//@src')[0].extract()
        app['Desc'] =  response.xpath('//div[@jsname="C4s9Ed"]/text()')[0].extract()
        app['Rating'] =  response.xpath('//div[@class="current-rating"]//@style')[0].extract().replace(';','').replace('width','').replace(' ','')
        app['Recommenders'] = '' 
        app['PosId'] =  ''
        app['AppType'] =  app['Title']+'/'+ app['genre']
        app['Lan'] =  response.url.split('=')[2]
        app['Country'] =  response.url.split('=')[2]
        app['fileSize'] =  ''
        app['genre2'] =  app['genre']
        app['name'] =  app['Title']
        app['GpTag'] =  ''
        # print (app['PkgName'],app['Title'],app['genre'],app['score'],
        #     app['ratingHistogram'],app['comp'],app['datePublished'], 
        #     app['numDownloads'],app['ratingValue'],app['contentRating'],
        #     app['Reviewers'],app['softwareVersion'],app['GpCategory'],
        #     app['GpCategory2'] , app['similarApps'], app['operatingSystems'],
        #     app['ads'],app['whatsNew'], app['inAppMsg'],
        #     app['price'],app['LogoUrl'],app['ClkUrl'],app['mail'],app['Thumbnails'],
        #     app['Desc'],app['Rating'],app['Recommenders'],app['PosId'],app['AppType'],
        #     app['Lan'], app['Country'],app['fileSize'],app['genre2'],app['name'],app['GpTag'])
        yield app
        




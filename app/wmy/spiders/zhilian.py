import math
import json
from scrapy.spiders import Spider

class zhilian(Spider):
    name = 'zhilian'
    keywords = 'php'
    pageSize = 100
    pageCurrent = 1
    url = "https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=719&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&sortType=salary&kw={}&kt=3&page={}"
    start_urls = [
        url.format(pageSize, keywords, pageCurrent)
    ]

    def parse(self, response):
        responseBody = json.loads(response.body)
        pageMax = math.ceil(responseBody['data']['numFound']/self.pageSize)
        for item in responseBody['data']['results']:
            yield item
        if responseBody['code'] == 200 and self.pageCurrent < pageMax:
            self.pageCurrent = self.pageCurrent + 1
            yield response.follow(self.url.format(self.pageSize, self.keywords, self.pageCurrent), self.parse)
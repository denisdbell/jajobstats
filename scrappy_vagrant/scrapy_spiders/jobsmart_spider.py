import scrapy

class JobSmartSpider(scrapy.Spider):
    name = 'jobsmart'

    start_urls = ['http://go-jamaica.com/jobsmart/']

    def parse(self, response):
        # follow links to job category pages
        for href in response.xpath("//a[contains(@href,'jobtitle')]/@href").extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_jobs)

	#Loop through each job category
    def parse_jobs(self, response):
        
	    for href in response.xpath("//a[contains(@href,'view_ad_details.php')]/@href"]/@href").extract():
		
			yield scrapy.Request(response.urljoin(href),
									 callback=self.parse_job_details)
	
	
	def parse_job_details(self, response):
		
			yield {
				'category': response.xpath("//td[@class='careerright']/table[2]/tr[2]/td[@class='careerdetail']/text()").extract()
	,
				'title': response.xpath("//td[@class='careerright']/table[2]/tr[1]/td[@class='careerheader']/b/text()").extract()
	,
				'description': response.xpath("//td[@class='careerright']/table[2]/tr[3]/td[@class='careerdetail']/text()").extract()
	,

				'qualifications': response.xpath("//td[@class='careerright']/table[2]/tr[4]/td[@class='careerdetail']/text()").extract()
			}
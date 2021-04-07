import scrapy

class Shopify(scrapy.Spider):
    http_user='someuser'
    http_pass='somepass'
    name='shop'
    start_urls=[]
    custom_settings={
        'DOWNLOAD_DELAY':1,
        'CONCURRENT_REQUESTS_PER_DOMAIN':1
    } 
    def __init__(self):
        for i in range(1,10):
            self.start_urls.append(f'https://myip.ms/browse/sites/{i}/own/376714')
      
    def parse(self, response):
        main=response.css('#sites_tbl')
        web_name=main.css('td:nth-child(2)')
        ip=main.css('td:nth-child(3)')
        host_owner=main.css('td:nth-child(4)')
        country=main.css('td:nth-child(5)')
        city=main.css('td:nth-child(6)').getall()
        rank=[]
        for x in response.css('span.bold.arial.grey').getall():
            if '#' in x:
                rank.append(x)
            else:
                pass
        value=[]
        for x in city:
            if 'cities' in x:
                value.append(x)
            else:
                value.append('None')
        for i in range(len(web_name)):
            yield{
                'website':web_name.css('a::text').getall()[i],
                'web_ip_addr':ip.css('a::text').getall()[i],
                'web_host_comp':host_owner.css('a::text').getall()[i],
                'web_host_country':country.css('a::text').getall()[i],
                'web_host_city':value[i],
                'World_Site_Popular_Rating':rank[i]
            }
        
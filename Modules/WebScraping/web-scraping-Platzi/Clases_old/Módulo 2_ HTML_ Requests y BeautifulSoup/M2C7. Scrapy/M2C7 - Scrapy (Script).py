import scrapy


class Spider12(scrapy.Spider):
    name = 'Spider12'
    allowed_domains = ['pagina12.com.ar']
    custom_settings = {'DEPTH_LIMIT': 1,
                       'FEED_FORMAT': 'json',
                       'FEED_URI': 'resultados.json'}
    start_urls = ['https://www.pagina12.com.ar/secciones/el-pais',
                  'https://www.pagina12.com.ar/secciones/economia',
                  'https://www.pagina12.com.ar/secciones/sociedad',
                  'https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos',
                  'https://www.pagina12.com.ar/secciones/ciencia',
                  'https://www.pagina12.com.ar/secciones/el-mundo',
                  'https://www.pagina12.com.ar/secciones/deportes',
                  'https://www.pagina12.com.ar/secciones/contratapa']
    # start_urls = ['https://www.pagina12.com.ar/secciones/el-pais']

    def parse(self, response):
        # Artículo promocionado
        nota_promocionada = response.xpath('//div[@class="featured-article__container"]//h2/a/@href').get()
        if nota_promocionada is not None:
            yield response.follow(nota_promocionada, callback=self.parse_nota)

        # Listado de notas
        notas = response.xpath('//ul[@class="article-list"]//li//a/@href').getall()
        for nota in notas:
            yield response.follow(nota, callback=self.parse_nota)

        # Link a próxima página
        next = response.xpath('//a[@class="pagination-btn-next"]/@href').get()
        if next is not None:
            yield response.follow(next, callback=self.parse)

    def parse_nota(self, response):
        # Parseo la nota
        titulo = response.xpath('//div[@class="article-title"]/text()').get()
        cuerpo = ''.join(response.xpath('//div[@class="article-text"]/p/text()').getall())
        yield {'url': response.url,
               'titulo': titulo,
               'cuerpo': cuerpo}


from scrapy.crawler import CrawlerProcess
process = CrawlerProcess()
process.crawl(Spider12)
process.start()

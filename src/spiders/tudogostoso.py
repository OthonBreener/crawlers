from scrapy import Request, Spider

from ..items import VeganRecipesItem


class TudogostosoSpider(Spider):
    name = 'tudogostoso'
    allowed_domains = ['tudogostoso.com.br']
    start_urls = [
        'https://www.tudogostoso.com.br/busca?q=vegana',
        'https://www.tudogostoso.com.br/busca?q=vegano',
        'https://www.tudogostoso.com.br/busca?q=vegan',
    ]

    def parse(self, response):
        '''Entrar em cada receita.'''
        links = response.xpath(
            '//div[@class="pagination"]/parent::div'
            '//a[@class="link row m-0"]/@href'
        ).getall()
        for link in links:
            yield Request(response.urljoin(link), callback=self.parse_recipes)

        '''Sistema de paginação.'''
        pagination = response.xpath(
            '//div[@class="pagination"]//a//@href'
        ).getall()
        for next in pagination:
            yield Request(response.urljoin(next), callback=self.parse)

    def parse_recipes(self, response):
        '''Parsear a receita.'''
        items = VeganRecipesItem()

        title = (
            response.xpath('//h1[@tabindex="0"]//text()')
            .get()
            .replace('\n', '')
        )
        image = response.css('img.pic::attr(src)').get()
        ingredients = '. '.join(
            response.xpath('//div[@id="info-user"]//ul//li//text()').getall()
        )
        preparation = ' '.join(
            response.xpath(
                '//div[@itemprop="recipeInstructions"]//ol//li//text()'
            ).getall()
        )
        time = response.css('time.dt-duration::text').get().replace('\n', ' ')

        items['title'] = title
        items['image'] = image
        items['ingredients'] = ingredients
        items['preparation'] = preparation
        items['time'] = time
        items['url'] = response.url

        yield items

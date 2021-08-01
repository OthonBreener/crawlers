from scrapy import Field, Item


class VeganRecipesItem(Item):
    title = Field()
    image = Field()
    ingredients = Field()
    preparation = Field()
    time = Field()
    url = Field()

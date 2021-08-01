BOT_NAME = 'vegan_recipes'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'src.pipelines.VeganRecipesPipeline': 300,
}

from .models import VeganRecipes


class VeganRecipesPipeline:
    def process_item(self, item, spider):
        if not VeganRecipes.table_exists():
            VeganRecipes.create_table()
        try:
            VeganRecipes.create(
                title=item['title'],
                image=item['image'],
                ingredients=item['ingredients'],
                preparation=item['preparation'],
                time=item['time'],
                url=item['url'],
            )
        except Exception as e:
            if str(e.args[0]) == '1062':
                print('repeated data, skip.')
            else:
                print(e.args[0], e.args[1])

        return item

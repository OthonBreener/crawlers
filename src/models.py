from peewee import Model, SqliteDatabase, TextField

db = SqliteDatabase('recipes.db')


class VeganRecipes(Model):
    title = TextField()
    image = TextField()
    ingredients = TextField()
    preparation = TextField()
    time = TextField()
    url = TextField(unique=True)

    class Meta:
        database = db

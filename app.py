from peewee import *

db = PostgresqlDatabase('beer', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Beer(BaseModel):
    name = CharField()
    brewery_type = CharField()
    street = CharField()
    city = CharField()
    state = CharField()
    postal_code = IntegerField()
    country = CharField()
    longitude = IntegerField()
    latitude = IntegerField()
    phone = IntegerField()
    website_url = CharField()


db.connect()
db.drop_tables([Beer])
db.create_tables([Beer])

Beer(name='test', brewery_type="moretest", street='testing', city="test",
     state="test", postal_code=20853, country="test", longitude=5, latitude=5, phone=3, website_url='test').save()

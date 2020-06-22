from peewee import *
import json
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
    postal_code = CharField()
    country = CharField()
    longitude = CharField()
    latitude = CharField()
    phone = CharField()
    website_url = CharField()


db.connect()
db.drop_tables([Beer])
db.create_tables([Beer])

with open('./Data.json') as f:
    data = json.load(f)


for beer in data.get('beers'):
    Beer(
        name=beer.get('name'), brewery_type=beer.get('brewery_type'),
        street=beer.get('street'), city=beer.get('city'),
        state=beer.get('state'), postal_code=beer.get('postal_code'),
        country=beer.get('country'), longitude=beer.get('longitude'),
        latitude=beer.get('latitude'), phone=beer.get('phone'),
        website_url=beer.get('website_url')).save()

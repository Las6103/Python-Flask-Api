from peewee import *
from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
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


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello! Welcome to the beer api! To find all the beers continue to localhost:5000/beers"


@app.route('/beers', methods=['GET'])
def beers():
    if request.method == 'GET':
        beer_list = []
        for beer in Beer.select():
            beer_list.append(model_to_dict(beer))
        return jsonify(beer_list)


@app.route('/beers/<_id>', methods=['GET', 'PUT', 'DELETE'])
def beer_id(_id):
    beer = Beer.get(Beer.id == _id)
    if request.method == 'GET':
        return jsonify(model_to_dict(beer))
    elif request.method == 'PUT':
        items = list(request.get_json().items())
        for item in items:
            beer_update = Beer.update(
                {item[0]: item[1]}).where(Beer.id == beer)
            beer_update.execute()

        return 'success'
    elif request.method == 'DELETE':
        beer.delete_instance()
        return 'success'


@app.route('/beers', methods=['POST'])
def post_beer_handler():
    beer = request.get_json()
    Beer(
        name=beer.get('name'), brewery_type=beer.get('brewery_type'),
        street=beer.get('street'), city=beer.get('city'),
        state=beer.get('state'), postal_code=beer.get('postal_code'),
        country=beer.get('country'), longitude=beer.get('longitude'),
        latitude=beer.get('latitude'), phone=beer.get('phone'),
        website_url=beer.get('website_url')).save()
    return beer


app.run(debug=True)

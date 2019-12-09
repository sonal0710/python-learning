from flask import Flask, Response, request
from db import mongo
from bson.json_util import dumps
from bson import ObjectId
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cities", methods=['GET'])
def get_all_cities():
    cities_details = mongo.db.cities.find()
    # output = []
    # for cities in cities_details.find():
    #     output.append(cities['cityStatus'])
    json_resp = dumps({'message': 'All City Details', 'result' : cities_details})
    resp = Response(json_resp, status=200, mimetype='application/json')
    return resp

@app.route("/cityByName/<cityName>", methods=['GET'])
def getCityByName(cityName):
    city_detail = mongo.db.cities.find({'city':cityName})
    json_resp = dumps({'message': 'City Detail', 'result' : city_detail})
    resp = Response(json_resp, status=200, mimetype='application/json')
    return resp

@app.route("/cityById/<cityId>", methods=['GET'])
def getCityById(cityId):
    city_detail = mongo.db.cities.find({'_id': ObjectId(cityId)})
    json_resp = dumps({'message': 'City Detail', 'result' : city_detail})
    resp = Response(json_resp, status=200, mimetype='application/json')
    return resp
    
@app.route("/insertCity", methods=['POST'])
def insertCity():
    cityDetails = { 'city': request.form['city'],
                    'state': request.form['state'],
                    'country': request.form['country']}
    insertCity = mongo.db.cities.insert(cityDetails)
    return "Inserted successfully"

if (__name__ == "__main__"):
    app.run(debug=True)
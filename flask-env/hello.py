from flask import Flask, jsonify
from db import mongo
from bson.json_util import dumps

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
    return dumps({'result' : cities_details})

if (__name__ == "__main__"):
    app.run(debug=True)
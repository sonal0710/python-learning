from flask import Flask, Response
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
    json_resp = dumps({'message': 'All City Details', 'result' : cities_details})
    resp = Response(json_resp, status=200, mimetype='application/json')
    return resp

if (__name__ == "__main__"):
    app.run(debug=True)
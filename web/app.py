from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import os

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://db:27017')
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
  'num_of_users': 0
})

class Visit(Resource):
  def get(self):
      prev_num = UserNum.find({})[0]['num_of_users']
      prev_num += 1
      UserNum.update({}, {'$set': {'num_of_users': prev_num}})
      return str('Hello user: ' + str(prev_num))

api.add_resource(Visit, '/hello')

@app.route('/')
def hello_world():
  return 'Hello'

if __name__ == "__main__":
  app.run(host='0.0.0.0')
from flask import Flask
from pymongo import MongoClient



app = Flask(__name__)
app.config['SECRET_KEY'] = '1b1b4504a9d02756ac0f6451d1f33df3'

conn = MongoClient('mongodb://db1:27017,db2:27017,db3:27017/?replicaSet=mongo-cluster')
db = conn.homeapp

from homeapp import routes
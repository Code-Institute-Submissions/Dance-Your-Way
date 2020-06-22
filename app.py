import os
import boto3
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from botocore.client import Config
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
ACCESS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')
app.secret_key = os.environ.get('secret_key')
app.config["MONGO_DBNAME"] = 'events_manager'
app.config["MONGO_URI"] = 'mongodb+srv://prelaunch:prelaunch@danceyourway-fmkw8.mongodb.net/events_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("index.html", events=mongo.db.events.find())


@app.route('/get_salsa_events')
def get_salsa_events():
    return render_template("salsa.html", events=mongo.db.events.find())


@app.route('/get_bachata_events')
def get_bachata_events():
    return render_template("bachata.html", events=mongo.db.events.find())


@app.route('/get_kizomba_events')
def get_kizomba_events():
    return render_template("kizomba.html", events=mongo.db.events.find())


@app.route('/style')
def style():
    return render_template("style.html")


@app.route('/add-event')
def add_event():
    return render_template("add-event.html", events=mongo.db.events.find())


@app.route('/insert-event', methods=['POST'])
def insert_event():
    events = mongo.db.events
    events.insert_one(request.form.to_dict())
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID,
                        aws_secret_access_key=ACCESS_SECRET_KEY)
    s3.Bucket('dance-your-way-event-images').put_object(
        Key=request.form['event_image'], Body=request.files['event_image_s3'])
    return redirect(url_for('event_added'))


@app.route('/event-added')
def event_added():
    return render_template("event-added.html", events=mongo.db.events.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

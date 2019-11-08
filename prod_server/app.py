import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Weather

@app.route("/")
def hello():
    return "Hello Cruel World!"

@app.route("/weather")
def get_all_weather_data():
    try:
        allWeather=Weather.query.all()
        return  jsonify([e.serialize() for e in allWeather])
    except Exception as e:
	    return(str(e))

@app.route("/weather/<id_>")
def get_weather_by_id(id_):
    try:
        weather=Weather.query.filter_by(id=id_).first()
        return jsonify(weather.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/weather/form")
def get_weather_by_id_form():
    return render_template("coolfrontpage.html", weathers=Weather.query.all())

if __name__ == '__main__':
    app.run()
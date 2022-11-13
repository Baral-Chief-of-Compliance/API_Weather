from flask import Flask, jsonify
import redis
from rq import Queue
from flask_cors import CORS
from weather_test import get_weather

app = Flask(__name__)
app.config.from_object(__name__)

r = redis.Redis()
q = Queue(connection=r)


CORS(app)


json_weather = get_weather()

@app.route('/weather/api/v1.0/Murmansk', methods = ['GET'])
def get_weather():
    return jsonify(json_weather)


if __name__ == '__main__':
    app.run(debug=True)
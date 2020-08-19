import yelp_request
import json
import logging
from flask import Flask
app = Flask(__name__)


from flask import request


@app.route('/')
def hello_world():
    user = request.args.get('user')
    return 'Hello ' + user + '!'


@app.route('/restaurant')
def restaurant():
    args = request.args

    if "location" in args:
        location = args.get('location')

        try:
            return yelp_request.get_yelp_loc(location)

        except Exception as e:
            logging.exception(e)
            return "Internal Server Error", 500


    elif "longitude" in args and "latitude" in args:
        longitude = args["longitude"]
        latitude = args["latitude"]

        # num = args.get('num')
        try:
            return yelp_request.get_yelp_rad(longitude, latitude, radius=4000)
        except Exception as e:
            logging.exception(e)
            return "Internal Server Error", 500

    elif "location" not in args:
        return "Error, did not return valid location", 400

    elif  "longitude" not in args or "latitude" not in args:
        return "Error, did not return valid longitude or latitude", 400

#random restaurant (parses thru random restaurant)

@app.route('/random')
def random():
    args = request.args
    text = ""

    if "location" in args:
        location = args.get('location')
        try:
            return yelp_request.randomRestaurantLoc(location)

        except Exception as e:
            logging.exception(e)
            return "Internal Server Error", 500

        #text =  yelp_request.get_yelp_loc(location)

    elif "longitude" in args and "latitude" in args:
        longitude = args["longitude"]
        latitude = args["latitude"]
        try:
            return yelp_request.randomRestaurantRad(longitude, latitude, radius=4000)

        except Exception as e:
            logging.exception(e)
            return "Internal Server Error", 500
        #text= yelp_request.get_yelp_rad(longitude, latitude, radius=4000)

    elif "location" not in args:
        return "Error, did not return valid location", 400

    elif "longitude" not in args or "latitude" not in args:
        return "Error, did not return valid longitude or latitude", 400


   # parsed_json = (json.loads(text))
   # print(json.dumps(parsed_json, indent=4, sort_keys = True))


@app.route("/")
def query():

    print(request.query_string)

    return "Thanks", 200
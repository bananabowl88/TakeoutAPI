import yelp_request
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

        return yelp_request.get_yelp_loc(location)

    elif "longitude" in args and "latitude" in args:
        longitude = args["longitude"]
        latitude = args["latitude"]

        # num = args.get('num')
        return yelp_request.get_yelp_rad(longitude, latitude, radius=4000)


    elif "location" not in args:
        return "Error, did not return valid location", 400

    elif  "longitude" not in args or "latitude" not in args:
        return "Error, did not return valid longitude or latitude", 400





@app.route('/rest')
def rest():
    args = request.args

    if "longitude" not in args or "latitude" not in args:
        return "Error, did not return valid longitude or latitude", 400

    longitude = args["longitude"]
    latitude = args["latitude"]



    #num = args.get('num')
    return yelp_request.get_yelp_rad(longitude, latitude, radius=4000)
    #'Your longitude is ' + longitude + ' and your latitude is ' + latitude





@app.route("/")
def query():

    print(request.query_string)

    return "Thanks", 200
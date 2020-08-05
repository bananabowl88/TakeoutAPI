from flask import Flask
app = Flask(__name__)


from flask import request


@app.route('/')
def hello_world():
    user = request.args.get('user')
    return 'Hello ' + user + '!'


@app.route('/restaurants')
def longitude():
    args = request.args

    num = args.get('num')
    return 'Your longitude is ' + num + '!'



@app.route('/restaurant')
def latitude():
    args = request.args


    longitude = args["longitude"]
    latitude = args["latitude"]

    #num = args.get('num')
    return 'Your longitude is ' + longitude + ' and your latitude is ' + latitude





@app.route("/")
def query():

    print(request.query_string)

    return "Thanks", 200
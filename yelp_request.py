import requests
import json
import random


with open('yelp_api_credentials.json') as file:
    apiData = json.load(file)
    apiKey = apiData["yelp_api_key"]
    header = {'Authorization': 'Bearer ' + str(apiKey)}


def get_yelp_loc(location):
    payload = {'term': 'food', 'location' : location}

    r = requests.get("https://api.yelp.com/v3/businesses/search",  params=payload, headers = header)
    return r.text

def get_yelp_rad(longitude, latitude, radius):
    payload = {"term": 'food', 'longitude': longitude, 'latitude': latitude, 'radius': radius}

    r = requests.get("https://api.yelp.com/v3/businesses/search",  params=payload, headers = header)
    return r.text

def randomRestaurantLoc(location):
    text = get_yelp_loc(location)
    data = json.loads(text)
    randNum = random.randint(0,len(data["businesses"]))
    #print(data["businesses"][randNum]["name"])
    return data["businesses"][randNum]

def randomRestaurantRad(longitude, latitude, radius):
    text = get_yelp_rad(longitude, latitude, radius)
    data = json.loads(text)
    randNum = random.randint(0, len(data["businesses"]))
    # print(data["businesses"][randNum]["name"])
    return data["businesses"][randNum]



if __name__ == "__main__":
    print("Executed when invoked directly")
    #print(get_yelp_loc("NYC"))
    #text = get_yelp_loc("NYC")
    #data = json.loads(text)
   # for i in data["businesses"]:
     #   print(i["name"])

    randomRestaurantLoc("NYC")
    #print(data["businesses"][0]["name"])
    #print(text[0])


#print(r.url)


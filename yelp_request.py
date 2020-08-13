import requests
from flask import Flask, render_template


app = Flask(__name__)

yelp_api_key = "UcIJVAd9xi0V1fFZp3bAA2AlxZWaAayRlSwTYyaSQ4JaEK_vTkeNr5_LSBW8AZrDLfnVybv1BSXXHWPCdfsecQOa4cQlqeRnrRNGW3LEloFv0ZVtH2SMffBztAtMW3Yx"
header = {'Authorization': 'Bearer UcIJVAd9xi0V1fFZp3bAA2AlxZWaAayRlSwTYyaSQ4JaEK_vTkeNr5_LSBW8AZrDLfnVybv1BSXXHWPCdfsecQOa4cQlqeRnrRNGW3LEloFv0ZVtH2SMffBztAtMW3Yx'}

def get_yelp_loc(location):
    payload = {'term': 'food', 'location' : location}

    r = requests.get("https://api.yelp.com/v3/businesses/search",  params=payload, headers = header)
    return r.text

def get_yelp_rad(longitude, latitude, radius):
    payload = {"term": 'food', 'longitude': longitude, 'latitude': latitude, 'radius': radius}
    r = requests.get("https://api.yelp.com/v3/businesses/search",  params=payload, headers = header)
    return r.text

#print(r.url)


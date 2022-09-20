import os
import requests, json
from requests.structures import CaseInsensitiveDict
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


# login required decorator from flask docs
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# function to look up furniture stores taking the address as argument
def lookup(address):
    try:
        api_key = os.environ.get('API_KEY')
        data_type = 'json'
        geocode_url = f"https://api.geoapify.com/v1/geocode/search?text={address}&format={data_type}&apiKey={api_key}"
        payload = {}
        headers = {}
        response = requests.get(geocode_url, headers=headers, data=payload)
    except:
        return None
    
 # use derived long and lat to derive places 
    try:    
        locations = response.json()
        long = locations['results'][0]['lon']
        lat = locations['results'][0]['lat']
        places_url = f"https://api.geoapify.com/v2/places?categories=commercial.furniture_and_interior&filter=circle:{long},{lat},5000&apiKey={api_key}"
        payload = {}
        headers = {}
        response = requests.get(places_url, headers=headers, data=payload)
        places = response.json()
    except:
        return None
    
    try:
        result = []
        for p in places['features']: 
            result.append({ "name" : p['properties']['name'], 
            "formatted" : p['properties']['formatted']
            })
        return result
            
    except:
        return None
            
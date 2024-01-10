#!/usr/bin/env python3

import reverse_geocoder as rg
import requests
from datetime import datetime


def main():

    issapi = requests.get("http://api.open-notify.org/iss-now.json").json()

    print("Current position of the ISS:")
    timestamp_value = issapi["timestamp"]
    dt_object = datetime.fromtimestamp(timestamp_value)
    formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)
    print("Lat:", issapi["iss_position"]["latitude"])
    print("Lon:", issapi["iss_position"]["longitude"])
    coords_tuple = (issapi["iss_position"]["latitude"], issapi["iss_position"]["longitude"])
    location = rg.search(coords_tuple, verbose=False)
    city = location[0]["name"]
    country = location[0]["cc"]
    print(city, country)
    


main()
#!/usr/bin/python3
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API")
print("API Key:", api_key)
## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
## def returncreds():
    ## first I want to grab my credentials
    ## with open("/home/student/mycode/nasa.creds", "r") as mycreds:
       ## nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    ## nasacreds = "api_key=" + nasacreds.strip("\n")
    ## return nasacreds

# this is our main function
def main():
    ## first grab credens
    api_key = os.getenv("NASA_API")
    print("API Key:", api_key)   
    ## update the date below, if you like
    startdate = input("Please enter a start date in this format (YYYY-MM-DD): ")

    ## the value below is not being used in this
    ## version of the script
    ## enddate = input("Please enter an end date in this format (YYYY-MM-DD): ")

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + api_key)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

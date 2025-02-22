"""
Library: requests
We can access APIs using requests library
"""
print("REST-API-1: SOME DUMMY API")
print("-"*20)
# -------------

import requests
api_response = requests.get("https://reqres.in/api/users?page=2")
api_data = api_response.json()

print("api_data:", api_data, end="\n\n")

print("type of api_data:", type(api_data), end="\n\n")

print("#"*40, end="\n\n")
##########################

print("REST-API-2: Accessing OUR API")
print("-"*20)
# -------------

try:
    import requests
    api_response = requests.get("http://127.0.0.1:5000/getdbdata")
    api_data = api_response.json()
    print("api_data:", api_data, end="\n\n")
    print("type of api_data:", type(api_data), end="\n\n")
except Exception as e:
    print("Error Details:", e)
    print("""
    Not able to access API, make sure to run
    my_rest_api_release_1.py
    """)

print("#"*40, end="\n\n")
##########################
import requests
import json

url = "https://api.snyk.io/api/v1/orgs"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'token API_KEY' #Documentation of how to generate an API_KEY https://docs.snyk.io/snyk-api-info/authentication-for-api
}

response = requests.get(url, headers = headers)

j = response.json()

print("Your Snyk orgs names and IDs are:")
for each in j['orgs']:
    print(each['name'], end = ' : ')
    print(each['id'])
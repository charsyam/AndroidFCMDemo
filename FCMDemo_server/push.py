import redis
import json
import requests
from oauth2client.service_account import ServiceAccountCredentials

rconn = redis.StrictRedis()

PROJECT_ID = "YOUR_PROJECT_ID"
BASE_URL = "https://fcm.googleapis.com"
FCM_ENDPOINT = "v1/projects/" + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + "/" + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
ACCOUNT_FILE = "YOUR_ACCOUNT_JSON_FILE"

API_KEY = rconn.get("apikey:fcmdemo").decode('utf-8')

def _get_access_token():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            ACCOUNT_FILE, SCOPES)
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token

# data to be sent to api 
token = rconn.get("token:charsyam").decode('utf-8')

data = {
        "message": {
            "token": token,
            "notification": {
                "title": "title",
                "body": "body"
            },
            "android": {
                "data": {
                    "title": "android",
                    "message": "test message"
                }
            }
        }
       }

print(data)
# sending post request and saving response as response object 
headers = {"content-type": "application/json", "Authorization": "Bearer {key}".format(key=_get_access_token())}

r = requests.post(url=FCM_URL, data=json.dumps(data), headers=headers) 
  
# extracting response text  
print(r.text)

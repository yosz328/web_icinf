import requests
import urllib
from urllib.parse import quote, urlencode
import json

def facebook_send_photo(mensaje,foto):
    
    token = "EAAGygZC1EsZAIBAMZA1139ZAVRcSZCvAWUalzjyhrGnOXsAGO61ZCndiYM3ytLo5lytXk2xfnrAOZAwCT4kbkxMMeCOWGizLFCHHZBAWL31LrEDxUpitq02ZCYnMWDecUuP096ikgOYnQjUZCRrkJRu9p25eS1jTWaX2sFg5rz3caYH0JCTZCxCsWje74BgeEayJLZAZA8ZCyBT0vtZAFLAIhHSUuOcgvbWSlXZC3IsSwuZCqgV5V8QZDZD"
    urlBase = "https://graph.facebook.com/2377986958907689/photos"
    data = {'url' : foto , 'caption' : mensaje , 'access_token' : token}
    r = requests.post(urlBase, data = json.dumps(data))
    print(r.json())
    return r.json()
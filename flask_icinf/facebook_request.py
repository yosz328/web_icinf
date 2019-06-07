import requests
import urllib
from urllib.parse import quote, urlencode

def facebook_send(mensaje):
    
    token = "EAAGygZC1EsZAIBAMZA1139ZAVRcSZCvAWUalzjyhrGnOXsAGO61ZCndiYM3ytLo5lytXk2xfnrAOZAwCT4kbkxMMeCOWGizLFCHHZBAWL31LrEDxUpitq02ZCYnMWDecUuP096ikgOYnQjUZCRrkJRu9p25eS1jTWaX2sFg5rz3caYH0JCTZCxCsWje74BgeEayJLZAZA8ZCyBT0vtZAFLAIhHSUuOcgvbWSlXZC3IsSwuZCqgV5V8QZDZD"
    urlBase = "https://graph.facebook.com/2377986958907689/feed/?message="
    urltok = "&access_token="

    urlBase = urlBase + mensaje + urltok + token
    print(urlBase)
    r = requests.post(urlBase)
    print(r.json())
    return r.json()

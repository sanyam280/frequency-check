import os
import requests

def get_token():
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET")
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]
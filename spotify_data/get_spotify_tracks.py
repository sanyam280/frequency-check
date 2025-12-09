import requests
import os
from get_access_token import get_token
from dotenv import load_dotenv



load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


token = get_token()
print("Access token: ",token)
playlist_id = "7MwgrmB2j0AqaJj9yGPYSB?si=7MwgrmB2j0AqaJj9yGPYSB"
url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(url, headers=headers)
r.raise_for_status()
response_dict = r.json()
with open("track_response.txt", "w") as file:
    file.write(str(response_dict.get('tracks').get('items')))
# print(response_dict.keys())
# print(response_dict.get('tracks').keys())
tracks_list = response_dict.get('tracks')

with open('tracks_list.txt', 'w') as file:  
    for idx,item in enumerate(tracks_list):
        track = tracks_list.get('items')[idx].get('track')
        track_name = track.get('name')
        # track_artist = track.get('artists')
        file.write(f"{track_name},  ")


print(tracks_list.get('items')[0].get('track').keys())
print(tracks_list.get('items')[0].get('track').get('track'))
print(tracks_list.get('items')[0].get('track').get('name'))

# print(response_dict.get('owner'))
# print(response_dict.get('name'))


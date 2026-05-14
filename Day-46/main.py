import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
response = requests.get(url)
songs_webpage = response.text

soup = BeautifulSoup(songs_webpage, "html.parser")

songs_list = []
songs = soup.find_all(name="h3", class_="chart-entry__title")
for song in songs:
    songs_list.append(song.get_text())
print(songs_list)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(playlists)

playlist_id = yt.create_playlist(
    title=f"{date} Billboard 100",
    description="Top 100 songs from Billboard",
    privacy_status="PRIVATE"
)
print(playlist_id)
song_video_ids = []

for song in songs_list:
    try:
        result = yt.search(query=song, filter="songs")
        video_id = result[0]["videoId"]
        song_video_ids.append(video_id)
        print(f"Added: {song}")
    except:
        print(f"{song} not found.")
yt.add_playlist_items(
    playlistId=playlist_id,
    videoIds=song_video_ids

)
                             
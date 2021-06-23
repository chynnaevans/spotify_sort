import spotify_secrets as sec
import tekore as tk

redirect_uri = "http://localhost:5000/callback"
conf = (sec.client_id, sec.client_secret,redirect_uri)
token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
playlist_id = "3lc4foebgTQXjrIdmZ7d90"

spotify = tk.Spotify(token)
playlist = spotify.playlist(playlist_id)

tracks = playlist.asbuiltin()["tracks"]["items"]
tracks.sort(key=lambda item: item["track"]["album"]["release_date"])

for track in tracks:
    print(track["track"]["album"]["release_date"] + "\n")

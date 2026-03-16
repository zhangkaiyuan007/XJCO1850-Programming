from flask import flash, redirect, render_template, request, url_for
from app import app
import csv
import os
import requests

# MusicBrainz API configuration
# We're using an API to get an image of the album - you will see more APIs next week!
MUSICBRAINZ_API_URL = "https://musicbrainz.org/ws/2/release/"
COVER_ART_ARCHIVE_URL = "https://coverartarchive.org/release/"


# Read in our songs from file
def get_songs():
    songs = []
    with  open(os.path.join(app.root_path, 'static', 'song_data.csv'), encoding='utf-8') as f:
        song_reader = csv.reader(f)
        for each in song_reader:
            songs.append(each)
    return songs


# Write out songs (used to persist changes)
def write_songs(songs):
    with open(os.path.join(app.root_path, 'static', 'song_data.csv'), mode="w", encoding="utf-8") as f:
        song_writer = csv.writer(f)
        for each in songs:
            song_writer.writerow(each)


# multiple routes to avoid 404s
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("home.html", title="Top 500 Songs - Home")


@app.route('/all_songs')
def all_songs():
    # accounting for header row
    songs = get_songs()[1:]
    return render_template("all_songs.html", title="Top 500 Songs - All", songs=songs)



@app.route('/song/<int:id>')
def song(id):
    song = get_songs()[id]
    album_title = song[3].split("(")[0]

    # pre-set this in case album not found.
    cover_url = None

    # make a request to Musicbrainz for the ID of an album
    response = requests.get(
        MUSICBRAINZ_API_URL,
        params={'query': f"release:{album_title}", 'fmt': 'json'},
        headers={'User-Agent': 'FlaskApp/1.0 (example@example.com)'}
    )
    data = response.json()

    # if we got a valid response..
    if data.get('releases'):
        release_id = data['releases'][0]['id']

        # Fetch cover art from Cover Art Archive
        cover_art_response = requests.get(f"{COVER_ART_ARCHIVE_URL}{release_id}")
        if cover_art_response.status_code == 200:
            cover_art_data = cover_art_response.json()
            cover_url = cover_art_data['images'][0]['image']

    return render_template("single_song.html", title=f"Top 500 Songs - {song[1]}", song=song, cover_url=cover_url)


@app.route("/like/<int:id>")
def like_song(id):
    songs = get_songs()
    if songs[id][10] == "False":
        songs[id][10] = "True"
    else:
        songs[id][10] = "False"
    write_songs(songs)
    # we have no separate page, so send them back to the song page
    return redirect(url_for("song", id=id))


# this needs completing - check
@app.route("/liked")
def view_liked():
    songs = get_songs()
    liked = []
    for each in songs:
        if each[10] == "True":
            liked.append(each)
    return render_template("liked.html", liked=liked, title="Top 500 Songs - Liked Songs")

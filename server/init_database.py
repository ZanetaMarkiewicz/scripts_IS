import os
from server.app import db
from server.models import Album

# Data to initialize database with
Albums = [
    {"artist": "Michael Jackson", "title": "Thriller",
     "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Michael_Jackson_-_Thriller.png/220px-Michael_Jackson_-_Thriller.png"},
    {"artist": "Linkin Park", "title": "Meteora",
     "image_url": "https://image.ceneostatic.pl/data/products/48665992/i-linkin-park-meteora-album-cover-sticker.jpg"},
]

# Delete database file if it exists currently
if os.path.exists("music_store.db"):
    os.remove("music_store.db")

# Create the database
db.create_all()

# populate the database
for album in Albums:
    a = Album(artist=album.get("artist"), title=album.get("title"), image_url=album.get("image_url"))
    db.session.add(a)

db.session.commit()

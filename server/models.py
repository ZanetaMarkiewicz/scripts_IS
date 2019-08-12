from server.app import db, ma
import datetime


class Album(db.Model):
    __tablename__ = "album"
    album_id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(64))
    title = db.Column(db.String(128))
    image_url = db.Column(db.String(255))
    last_edited_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

# pochodzi od marshmallow, pozwala nam wyluskac tylko to co nas interesuje z klasy
class AlbumSchema(ma.Schema):
    class Meta:
        # model = Album,
        fields = ("album_id", "artist", "title", "image_url", "last_edited_at")
        sqla_session = db.session

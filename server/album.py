from server.app import db
from server.models import Album, AlbumSchema
from flask import make_response, abort


def read_all():
    """
    This function responds to a request for /api/album
    with the lists of available albums
    :return:        json string of list of albums
    """
    # Create the list of people from our data
    albums = Album.query.order_by(Album.artist).all()

    # Serialize the data for the response
    album_schema = AlbumSchema(many=True)
    dump = album_schema.dump(albums)
    data = dump.data
    return data


def read_one(album_id):
    """
    This function responds to a request for /api/album/{album_id}
    with one matching album from albums
    :param album_id:   Id of album to find
    :return:            album with passed id (if founded)
    """
    # Get the album from db
    album = Album.query.filter(Album.album_id == album_id).one_or_none()

    if album is not None:

        # Serialize the data for the response
        album_schema = AlbumSchema()
        data = album_schema.dump(album).data
        return data

    # Otherwise, nope, didn't find that album
    else:
        abort(
            404,
            "Album not found for Id: {album_id}".format(album_id=album_id),
        )


def create(album):
    """
    This function creates a new album
    based on the passed data
    :param album:  album to create in people structure
    :return:        201 on success, 406 on album exists
    """
    artist = album.get("artist")
    title = album.get("title")
    image_url = album.get("image_url")

    existing_album = (
        Album.query.filter(Album.artist == artist)
            .filter(Album.title == title)
            .one_or_none()
    )

    if existing_album is None:

        # Create a album instance using the schema
        schema = AlbumSchema()
        new_album = Album(artist=album["artist"], title=album["title"], image_url=album["image_url"])

        # Add the album to the database
        db.session.add(new_album)
        db.session.commit()

        # Serialize and return the newly created album in the response
        data = schema.dump(new_album).data

        return data, 201

    # Album exists already
    else:
        abort(
            409,
            f"Album {artist}: {title} exists already"
        )


def update(album_id, album):
    """
    This function updates an existing album
    Throws an error if an album
    already exists in the database.
    :param album_id:   Id of the album to update
    :param album:      new data of album
    :return:            updated album data
    """

    album_to_update = Album.query.filter(
        Album.album_id == album_id
    ).one_or_none()

    # Check if we're trying to create duplicates in db
    artist = album.get("artist")
    title = album.get("title")
    image_url = album.get("image_url")

    existing_album = (
        Album.query.filter(Album.artist == artist)
            .filter(Album.title == title)
            .one_or_none()
    )

    if album_to_update is None:
        abort(
            404,
            "Album not found for Id: {album_id}".format(album_id=album_id),
        )

    # Would our update create a duplicate?
    elif (
            existing_album is not None and existing_album.album_id != album_id
    ):
        abort(
            409,
            f"Album {artist}: {title} exists already"
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed data into a db object
        schema = AlbumSchema()
        update_album_data = Album(artist=artist, title=title, image_url=image_url)

        # Set the id to the album we want to update
        update_album_data.album_id = album_to_update.album_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update_album_data)
        db.session.commit()

        # return updated album
        data = schema.dump(update_album_data).data

        return data, 200


def delete(album_id):
    """
    This function deletes an album
    :param album_id:   Id of the album to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the album from db
    album = Album.query.filter(Album.album_id == album_id).one_or_none()

    if album is not None:
        db.session.delete(album)
        db.session.commit()
        return make_response(
            f"Album with id {album_id} deleted", 200
        )

    # Didn't find that album
    else:
        abort(
            404,
            f"Album with id {album_id} not found"
        )

from flask import render_template
from server.app import app_connexion
from server.models import Album

# Get the application instance
connex_app = app_connexion

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "index.html"
    """
    albums = Album.query.order_by(Album.artist).all()

    # Serialize the data for the response
    # album_schema = AlbumSchema(many=True)
    # dump = album_schema.dump(albums)
    # data = dump.data

    return render_template("index.html", albums=albums)


if __name__ == "__main__":
    connex_app.run(port=8080, debug=True)

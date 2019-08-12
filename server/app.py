import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap

# moja sciezka
main_directory = os.path.abspath(os.path.dirname(__file__))

# generowanie nowej aplikacji
app_connexion = connexion.App(__name__, specification_dir=main_directory)

# dozwala na to aby flask dzialal na tej applikacji
app = app_connexion.app
# dodaje style
Bootstrap(app)

# database path
sqlite_path = "sqlite:///" + os.path.join(main_directory, "music_store.db")

# Configure the SqlAlchemy part of the app instance
# sqlalch bedzie wlaczone, gdyby nie bylo SQLalchemi to musielibysmy poslugiwac sie zwyklym sql
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_path
# sqlalch jest wstanie trackowac i zapisywac kazdy kolejny krok,
# na nasze potrzeby wylaczamy ta opcje
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# sql alchemy orm to communicate with sqlite db
db = SQLAlchemy(app)

# marshmallow init
ma = Marshmallow(app)

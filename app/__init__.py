from flask import Flask
from .config import Config, basedir
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = f"{basedir}/uploads"
migrate = Migrate(app,db,compare_type=True)

from .routes import *
from .models import *
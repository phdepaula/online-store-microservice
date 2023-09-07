from flask_openapi3 import Info

from database.database import Database
from resources.settings import Settings

INFORMATION = Info(title="Online Store", version="1.0.0")
SECRET_KEY = "Advanced Backend Development"
PORT = 5000
HOST = "0.0.0.0"

flask_settings = Settings(
    information=INFORMATION, secret_key=SECRET_KEY, port=PORT, host=HOST
)
flask_settings.generate_app()

app = flask_settings.app
database = Database()

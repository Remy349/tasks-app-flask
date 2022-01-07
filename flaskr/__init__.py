from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from flaskr import routes
from flaskr import auth

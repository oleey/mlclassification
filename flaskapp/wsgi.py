

from app import create_app
from config import BaseConfiguration as Config

app = create_app(Config)
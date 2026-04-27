from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from src.models.user_model import User


URL = "sqlite:///./arch-project.db"

engine = create_engine(URL, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

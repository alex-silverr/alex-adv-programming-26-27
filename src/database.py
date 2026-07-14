import datetime
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from src.settings import SQLALCHEMY_DATABASE_URL
import src.connect as ct

# -------------------------------
# Base from https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# Seems to be an SQLAlchemy thing but I don't understand the workings of it super well
class Base(DeclarativeBase):
    pass
# --------------------------------


dbeng = create_engine(SQLALCHEMY_DATABASE_URL) 
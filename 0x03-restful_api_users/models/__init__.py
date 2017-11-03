#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from models.user import User
from models.user_session import UserSession
from models.base_model import BaseModel, Base

host = os.environ.get('HBNB_YELP_MYSQL_HOST')
user = os.environ.get('HBNB_YELP_MYSQL_USER')
password = os.environ.get('HBNB_YELP_MYSQL_PWD')
db = os.environ.get('HBNB_YELP_MYSQL_DB')
env = os.environ.get('HBNB_YELP_ENV')

db_url = "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, db)
db_engine = create_engine(db_url)

if env == "test":
    Base.metadata.drop_all(db_engine)

Base.metadata.create_all(db_engine)

"""instance of SQLAlchemy Session"""
db_session = scoped_session(
    sessionmaker(bind=db_engine, expire_on_commit=False)
)

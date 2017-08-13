#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.user import User

host = os.environ.get('HBNB_YELP_MYSQL_HOST')
user = os.environ.get('HBNB_YELP_MYSQL_USER')
password = os.environ.get('HBNB_YELP_MYSQL_PWD')
db = os.environ.get('HBNB_YELP_MYSQL_DB')
env = os.environ.get('HBNB_YELP_ENV')

db_url = "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, db)
db_engine = create_engine(db_url)

if env == "test":
    db_engine.drop_all()

User.metadata.create_all(db_engine)

"""instance of SQLAlchemy Session"""
db_session = scoped_session(
    sessionmaker(bind=db_engine, expire_on_commit=False)
)

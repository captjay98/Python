#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://captjay98:81651515@localhost/industry")
Session = sessionmaker(bind=engine)
Base = declarative_base()



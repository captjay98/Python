#!/usr/bin/python3
"""Creates a Base Class
    an engine and session"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


url = "mysql://captjay98:81651515@localhost/final"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


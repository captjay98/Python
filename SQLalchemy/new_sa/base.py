#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://captjay98:81651515@localhost/music', echo=True)

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'

    id =  Column(Integer, primary_key=True)
    real_name = Column(String(50))
    stage_name = Column(String(50))

    def __repr__(self):
        return f"{real_name} {stage_name}"

Base.metadata.create_all(engine)

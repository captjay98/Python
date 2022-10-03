#!/usr/bin/python3

from base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Artist(Base):
    __tablename__ = 'artists'
    '''
    id = Column(Integer, primary_key=True)
    real_name = Column(String(100), nullable=False)
    stage_name = Column(String(100), nullable=False)
    added_on = Column(DateTime(), default=datetime.now)
    album = relationship('Album', backref='albums')
    '''
    id = Column(Integer(), primary_key=True)
    real_name = Column(String(100), nullable=False)
    stage_name = Column(String(100), nullable=False)
    albums = relationship("Album", backref="album")
    song = relationship("Song", backref="song")

    def __init__(self, real_name, stage_name):
        self.real_name = real_name
        self.stage_name = stage_name

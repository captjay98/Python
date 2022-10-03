#!/usr/bin/python3

from base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Album(Base):
    __tablename__ = 'albums'
    '''

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    release_year = Column(Integer, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    '''
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    release_year = Column(Integer(), nullable=False)
    artist_id = Column(Integer(), ForeignKey('artists.id'))

    def __init__(self, name, release_year, artist_id):
        self.name = name
        self.release_year = release_year
        self.artist_id = artist_id

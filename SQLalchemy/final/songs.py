#!/usr/bin/python3

from base import Base
from song_artists import song_artist
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Song(Base):
    __tablename__ = 'songs'
    '''
        id = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=False)
        album_id = Column(Integer, ForeignKey('albums.id'))
        artist = relationship("Artist", secondary=song_artist)
    '''
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    album_id = Column(Integer, ForeignKey('albums.id'))

    def __init__(self, name, album_id):
        self.name = name
        self.album_id = album_id

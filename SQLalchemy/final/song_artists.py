#!/usr/bin/python3
from base import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

song_artist = Table('song_artist', Base.metadata,
        Column('artist.id', Integer(), ForeignKey("artists.id")),
        Column('song_id', Integer(), ForeignKey('songs.id'))
)

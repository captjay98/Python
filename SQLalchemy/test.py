#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, ForeignKey, Integer, String, Column, Text, DateTime, Boolean
from datetime import datetime

engine = create_engine("mysql://captjay98:81651515@localhost/play")
engine.connect()

metadata = MetaData()


artists = Table('artists', metadata,
                Column('id', Integer(), primary_key=True, autoincrement=True),
                Column('name', String(55), nullable=False),
                Column('Entered_at', DateTime(), default=datetime.now),
                )

albums = Table('albums', metadata,
                Column('id', Integer(), primary_key=True),
                Column('name', Text(), nullable=False),
                Column('release_year', Integer(), nullable=False),
                Column('artist_id', ForeignKey("artists.id")),
                )
metadata.create_all(engine)

for t in metadata.tables:
    print(metadata.tables[t])

print('-------------')  

for t in metadata.sorted_tables:
    print(t.name)

print(albums.columns)         # return a list of columns
print(albums.c)               # same as albums.columns
print(albums.foreign_keys)    # returns a set containing foreign keys on the table
print(albums.primary_key)     # returns the primary key of the table
print(albums.metadata)        # get the MetaData object from the table
print(albums.columns.release_year.name)     # returns the name of the column




engine = create_engine("mysql://captjay98:81651515@localhost/market")

Base = declarative_base()
metadata = MetaData()


class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String(55), nullable=False, unique=True, index=True)
    added_on = Column(DateTime(), default=datetime.now())
    albums = relationship("Album", backref='album')
    songs = relationship("Song", backref='song')


class Album(object):
    __tablename__ = 'albums'
    id =  Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False, index=True)
     
    artist_id = Column(ForeignKey('artists.id'))
    songs = relationship("Song")
    artist  = relationship("Artist")

class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    album = Column(ForeignKey('albums.id'), nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'))
    album_id = Column(Integer, ForeignKey('albums.id'))

class Song(Base):
    __tablename__ = 'songs'
    id =  Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    album_id = Column(Integer(), ForeignKey('album.id'))
    artist_id = Column(Integer(), ForeignKey('artist.id'))
Base.metadata.create_all(engine)
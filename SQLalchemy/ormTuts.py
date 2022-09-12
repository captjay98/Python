#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker

from datetime import datetime


engine = create_engine("mysql://captjay98:81651515@localhost/tuts")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = MetaData()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer(), primary_key=True)
    real_name = Column(String(100), nullable=False)
    stage_name = Column(String(100), nullable=False)
    added_on = Column(DateTime(), default=datetime.now)
    albums = relationship("Album", backref="album")
    song = relationship("Song", backref="song")


class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    release_year = Column(Integer(), nullable=False)
    artist_id = Column(Integer(), ForeignKey('artists.id'))


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    album_id = Column(Integer, ForeignKey('albums.id'))

#Base.metadata.create_all(engine)


wiz = Artist( real_name = 'Wizkid Ayodeji Ibrahim Balogub',
                    stage_name = 'Big Wiz'
                    )

weeknd = Artist( real_name = 'Abel Tsefaye',
                            stage_name = 'The Weeknd',
                            )
'''
print(wiz.stage_name)
print(weeknd.real_name)
'''
#session.add_all([wiz, weeknd])

mil = Album(name = 'Made in Lagos',
                    release_year = 2020,
                    artist_id  = 1)

bbtm = Album(name = 'Beauty Behind the Madness',
                        release_year =  2014,
                        artist_id = 2)

#session.add_all([mil, bbtm])


t1 = Song(name = 'Reckless',
          artist_id = 1,
          album_id = 1)
t2 = Song(name = 'longtime',
          artist_id = 1,
          album_id = 1)

t3 = Song(name = 'Acquainted',
          artist_id = 2,
          album_id = 2)

t4 = Song(name = 'Losers',
          artist_id = 2,
          album_id = 2)

#session.add_all([t1, t2, t3, t4])


sasha = Artist( real_name = 'Sasha Sloan',
                    stage_name = 'Sad Girl '
                    )

taylor = Artist( real_name = 'Taylor Swift',
                            stage_name = 'Crazy Girl',
                            )

ape = Artist( real_name = 'Burna Boy',
                    stage_name = 'African Giant')
#session.add_all([sasha, taylor, ape])

sad= Album(name = 'Sad girl Sloan',
                    release_year = 2019,
                    artist_id  = 3)

tbest = Album(name = '1989',
                        release_year =  2014,
                        artist_id = 4)

ld = Album(name = 'Love Damini',
                    release_year = 2022,
                    artist_id  = 5)

ss = Album(name = 'SuperStar',
                        release_year =  2011,
                        artist_id = 1)

#session.add_all([sad, tbest, ld, ss])


t5 = Song(name = 'Sweet One',
          artist_id = 1,
          album_id = 1)
t6 = Song(name = 'Shake it off',
          artist_id = 4,
          album_id = 4)

t7 = Song(name = 'It\'s Plenty ',
          artist_id = 5,
          album_id = 5)

t8 = Song(name = 'Too Sad to Cry',
          artist_id = 3,
          album_id = 3)

t9 = Song(name = 'Essence ft Tens',
          artist_id = 1,
          album_id = 1)
t10 = Song(name = 'Call my name',
          artist_id = 1,
          album_id = 6)

t11 = Song(name = 'Wad up',
          artist_id = 1,
          album_id = 6)

t12 = Song(name = 'The hills',
          artist_id = 2,
          album_id = 2)
#session.add_all([t5, t6, t7, t8, t9, t10, t11, t12])
#session.commit()

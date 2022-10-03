#!/usr/bin/python3

from artists import Artist
from albums import Album
from songs import Song
from song_artists import song_artist
from writers import Writer
from base import Base, session, engine

Base.metadata.create_all(engine)

"""Artists"""
wiz = Artist('Wizkid Ayodeji Ibrahim Balogun','Big Wiz')
taylor = Artist('Taylor Swift','Crazy Girl')
weekend = Artist( real_name = 'Abel Tsefaye', stage_name = 'The Weeknd')
sasha = Artist( real_name = 'Sasha Sloan', stage_name = 'Sad Girl')
ape = Artist("Burna Boy", "African Giant")
tems = Artist("Temilade", "Tems")

skepta = Artist("Skeptagram", "skepta")

"""
session.add_all([wiz, taylor, weekend, sasha, ape, tems])

Albums

mil = Album('Made in Lagos', 2020, 1)

bbtm = Album('Beauty Behind the Madness', 2014, 2)

sad = Album('Sad girl Sloan',2019, 3)

tb = Album(name = '1989', release_year =  2014, artist_id = 4)

ld = Album(name = 'Love Damini', release_year = 2022, artist_id  = 5)

ss = Album(name = 'SuperStar', release_year =  2011, artist_id = 1)

session.add_all([mil, bbtm, ld, sad, tb, ss])
"""


"""writers

wr1 = Writer('Captain', True, wiz)
wr2 = Writer('Goat', True, ape)
wr3 = Writer('Okay', False, taylor)

session.add_all([wr1, wr2, wr3])
"""

"""Tracks"""

t1 = Song('Reckless', 1)
t1.artists = [wiz]

t2 = Song('longtime', 1)
t2.artists = [wiz, skepta]

t3 = Song('Acquainted',2)
t3.artists = [weekend]

t4 = Song('Losers', 2)
t4.artists = [weekend]

t5 = Song(name = 'Sweet One',album_id = 1)
t5.artists = [wiz]

t6 = Song(name = 'Shake it off', album_id = 4)
t6.artists = [taylor]

t7 = Song(name = 'It\'s Plenty ',album_id = 5)
t7.artists = [ape]

t8 = Song(name = 'Too Sad to Cry', album_id = 3)
t8.artists = [sasha]

t9 = Song(name = 'Essence ft Tems', album_id = 1)
t9.artists = [wiz, tems]

t10 = Song(name = 'Call my name', album_id = 6)
t10.artists = [wiz]

t11 = Song(name = 'Wad up', album_id = 6)
t11.artists = [wiz]

t12 = Song(name = 'The hills', album_id = 2)
t12.artists = [weekend]


session.add_all([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12])


session.commit()
session.close()

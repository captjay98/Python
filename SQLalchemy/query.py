#!/usr/bin/python3

from ormTuts import *
'''
data = session.query(Album.name, Album.artist_id).all()
session.query(Artist.stage_name)
session.query(Album).all()
session.query(Song.name)


for item in data:
    print(item)


print(session.query(Song).count())
session.query(Album).first()
session.query(Song).get(9)
'''

print(session.query(Song).filter(Song.name =='Too Sad to Cry').all())
print(session.query(Song).filter(Song.name == 'Too Sad to Cry'))
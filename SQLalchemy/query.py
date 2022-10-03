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

print(session.query(Song).filter(Song.name =='Too Sad to Cry').all())
print(session.query(Song).filter(Song.name == 'Too Sad to Cry'))
data = session.query(Artist.stage_name).join(Song.name).all()

for item in data:
    print(Artist.stage_name, Album.name)
'''

data = session.query(Artist, Album, Song).filter(Artist.id == Album.artist_id).all()
for item, it, ik in data:
    print("{:^5s} - {:^5s}".format(item.stage_name, it.name))    

d = session.query(Album, Song).filter(Album.id == Song.album_id).all()

for i, j in d:
    print(i.name, j.name)

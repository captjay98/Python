#!/usr/bin/python3

from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date

session = Session()
'''
movies = session.query(Movie).all()

for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('\n')
actors = session.query(Actor).all()

for actor in actors:
    print(actor.name )
'''

movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).all()

for movie in movies:
    print(f'{movie.title} was released recently')

the_rock_movies = session.query(Movie).join(Actor, Movie.actors)\
        .filter(Actor.name == 'Dwayne Johnson').all()

for movie in the_rock_movies:
    print(f'The Rock was in {movie.title}')

glendale_stars = session.query(Actor)\
        .join(ContactDetails)\
        .filter(ContactDetails.address.ilike('%glendale%')).all()

for actor in glendale_stars:
    print(f'{actor.name} has a house in glendale')


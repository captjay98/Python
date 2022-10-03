#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from base import Base
from sqlalchemy.orm import relationship


movies_actors_association = Table(
        'movies_actors', Base.metadata,
        Column('Movie_id', Integer, ForeignKey('movies.id')),
        Column('actor_id', Integer, ForeignKey('actors.id'))
        )

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movies_actors_association)


    def __init__(self, title, release):
        self.title = title
        self.release_date = release

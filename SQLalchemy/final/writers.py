#!/usr/bin/python3

from base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import String, Column, Integer, Boolean, ForeignKey

class Writer(Base):
    __tablename__ = 'writers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    active = Column(Boolean)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    artist = relationship("Artist", backref=backref("writer", uselist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor


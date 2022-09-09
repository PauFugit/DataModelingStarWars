import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    password = Column(String(250))
    inscription_date = Column(String(250))
    name = Column(String(250))
    lastname = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column
    climate = Column
    surface_water = Column
    population = Column

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column
    director = Column
    producer = Column
    release_date = Column

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column
    model = Column
    manufacturer = Column
    cost_in_credits = Column
    crew = Column
    passengers = Column 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
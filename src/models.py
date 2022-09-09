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
    user_name = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
   

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    height = Column(String(50))
    mass = Column(String(50))
    eye_color = Column(String(20))
    birth_year = Column(String(50))
    gender = Column(String(20))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    diameter = Column(Integer)
    climate = Column(String(100))
    surface_water = Column(String(50))
    population = Column(Integer)

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    model = Column(String(100), unique=True)
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cardo_capacity = Column(Integer)



    class Favorite_character(Base):
        __tablename__= 'favorite_characters'
        id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
        user_id=Column(Integer, ForeignKey('user.id'), nullable=False)


    class favorite_planet(Base):
        __tablename__='favorite_planets'
        id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    class favorite_starship(Base):
        __tablename__='favorite_starships'
        id= Column(Integer, ForeignKey('starships.id'), primary_key=True)
        user_id=Column(Integer, ForeignKey('user.id'), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
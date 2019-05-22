from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from tabledef import *
from movie_tabledef import *
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

class Currentwatching(Base):

	__tablename__ = "currentlywatching"
	id = Column(Integer, primary_key=True)
	email     = Column(String,ForeignKey(user.email))
	watching  = Column(String,ForeignKey(movie.name))
	 

def __init__(self,email,watching):

	self.self=self
	self.email = email
	self.watching = watching

	 
# create tables
Base.metadata.create_all(engine)
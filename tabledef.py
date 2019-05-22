from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

 
engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

class User(Base):

	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	firstname = Column(String)
	lastname  = Column(String)
	username  = Column(String)
	email     = Column(String)
	password  = Column(String)
	 

def __init__(self,firstname,lastname,email, username, password):

	self.self=self
	self.firstname = firstname
	self.lastname = lastname
	self.username = username
	self.email = email
	self.password = password
	 
# create tables
Base.metadata.create_all(engine)
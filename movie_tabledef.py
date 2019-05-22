from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os
engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

video_files=[]
for root, dirs, files in os.walk("static/video", topdown=False):
	for name in files:
		#temporary fix to only grab mp4 files
		if name.find("mp4")!= -1:
			video_files.append([name,os.path.join(root, name)])
			
print(video_files)

class Movie(Base):

	__tablename__ = "movie"
	id = Column(Integer, primary_key=True)
	movie_title = Column(String)
	movie_path  = Column(String)
	movie_releasedate     = Column(String)
	movie_duration    = Column(String)
	 

def __init__(self,movie_title,movie_path, movie_releasedate,movie_duration):

	
	self.self=self
	self.movie_title = movie_title
	self.movie_path = movie_path
	self.movie_releasedate = movie_releasedate
	self.movie_duration = movie_duration

	 
# create tables
Base.metadata.create_all(engine)
import os
import time
from moviepy.editor import VideoFileClip
from movie_tabledef import *

from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///tutorial.db', echo=True)
Session = sessionmaker(bind=engine)
s = Session()
video_files=[]
path=[]
# for root, dirs, files in os.walk("static/video", topdown=False):
	# for name in files:
		# if name.find("mp4")!= -1:
			# video_files.append([name,os.path.join(root, name)])
			# print([item[0] for item in video_files])
			# #print(video_files)
			# time.sleep(3)


for root, dirs, files in os.walk("static/video", topdown=False):
	for name in files:
		#temporary fix to only grab mp4 files
		if name.find("mp4")!= -1:
			movie = Movie(
				movie_title=str(name),
				movie_path=str(os.path.join(root, name)),
				movie_releasedate="",
				movie_duration=str(VideoFileClip(os.path.join(root, name)).duration))

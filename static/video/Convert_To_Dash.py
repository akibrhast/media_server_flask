import os
import subprocess
import time
import win32file #imported to be used for os.remove(path), and not result in a permission denied error .
import sys
from win10toast import ToastNotifier
video_files=[]
tittle = []
path = []
roots = []
toaster = ToastNotifier()


console_timer_in_seconds = 10
desktop_notification_message = "New conversion starting in {:2d} seconds. Stop the program now, or wait until next notification."


def consoletimer(console_timer_in_seconds):
	for remaining in range(console_timer_in_seconds, -1, -1):
		sys.stdout.write("\r")
		sys.stdout.write(desktop_notification_message.format(remaining))
		sys.stdout.flush()
		time.sleep(1)
		

def createlist():
	for root, dirs, files in os.walk("Movies", topdown=False):
		roots.append(root)
		for name in files:
			#temporary fix to only grab mp4 files
			if name.find("mp4")!=-1 and name.find("dash") == -1:
				video_files.append([name,os.path.join(root, name)])
				
def separatelist():				
	for tittle1,path1 in video_files:
		tittle.append(tittle1)
		path.append(path1)

def convertfile():
	for tittle1,path1 in video_files:
		print("\nStarting Conversion Process of: ")
		print("	#NAME: " + tittle1)
		print("	#LOCATION: " + path1)
		subprocess.call(["MP4Box","-dash", "1000", path1,"-out",path1])
		print("Deleting file: " + tittle1)
		win32file.SetFileAttributes(path1, win32file.FILE_ATTRIBUTE_NORMAL) # convert file attribute to NORMAL so, that it can be removed using  os.remove
		os.remove(path1)
		print("File deleted")
		toaster.show_toast("CONVERSION NEWS:","New Conversion starting in " + str(console_timer_in_seconds) + " seconds!!!",duration=console_timer_in_seconds,threaded=True)
		consoletimer(console_timer_in_seconds)

createlist()
convertfile()
import os,time,win32file,sys,subprocess,re,click
root_info=[]
root_info_dst=[]
dirs_info=[]
files_info=[]
movie_files_path=[]

def createlist():
	for root, dirs, files in os.walk("Movies", topdown=False):
		root_info.append(root)
		dirs_info.append(dirs)
		files_info.append(files)

def createDeepPaths():
	for root, dirs, files in os.walk("Movies", topdown=False):
		for name in files:
			movie_files_path.append(os.path.join(root, name))




def formatNames(filepathlist):
	for names in range(len(filepathlist)):
		temp_names = filepathlist[names].replace("  "," ")
		temp_names = filepathlist[names].replace(" ",".")
		temp_names = re.sub("\(([^()]*)\)","",temp_names) # remove everything inside parenthesis, including
		temp_names = re.sub("\[([^()]*)\]","",temp_names) # remove everything inside brackets, including
		temp_names = temp_names.rstrip(".")
		root_info_dst.append(temp_names)
	srcDst = dict(zip(filepathlist,root_info_dst))
	return srcDst


def clean_dir_names(srcDst):
	for src,dst in srcDst.items():
		if src != dst:
			print(src)
			print(dst)
			os.rename(src,dst)
		else:
    			pass
		


createDeepPaths()

clean_dir_names(formatNames(movie_files_path))
'''
def help():
	print("Avialable Functions:")
	print("1. createlist()")
	print("		Uses os.walk to traverse the current directory by default")
	print("		and create the following lists")
	print("			""root_info"" ")
	print("			""dirs_info"" ")
	print("			""files_info"" ")
'''
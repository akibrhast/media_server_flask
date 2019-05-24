import os,time,win32file,sys,subprocess,re,click
root_info=[]
root_info_dst=[]
dirs_info=[]
files_info=[]


def createlist():
	for root, dirs, files in os.walk("Movies", topdown=False):
		root_info.append(root)
		dirs_info.append(dirs)
		files_info.append(files)


createlist()
for names in range(len(root_info)):
	temp_names = root_info[names].replace("  "," ")
	temp_names = root_info[names].replace(" ",".")
	temp_names = re.sub("\(([^()]*)\)","",temp_names) # remove everything inside parenthesis, including
	temp_names = re.sub("\[([^()]*)\]","",temp_names) # remove everything inside brackets, including
	temp_names = temp_names.rstrip(".")
	root_info_dst.append(temp_names)
	
srcDst = dict(zip(root_info,root_info_dst))


def clean_dir_names():
	for src,dst in srcDst.items():
		os.rename(src,dst)

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
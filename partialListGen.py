import time
import os

examplie_list = [numbers for numbers in range(0,5000)]

def partialListGen():
	for i in range(0,len(examplie_list),10):
		yield examplie_list[i:i+10]
		
partialList=partialListGen()
next(partialList)


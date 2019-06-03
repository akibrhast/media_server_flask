import os, time,click


@click.command()
@click.option('-p','--path', default='.',help='Directory to be watched.')
def watchdirectorychange(path):
	"""Simple function that watches and notifies changes to the specified directory, defaults to current directory. """
	before = dict ([(f, None) for f in os.listdir (path)]) #Initial Directory State
	while 1:
		time.sleep (5)
		after = dict ([(f, None) for f in os.listdir (path)]) # Directory state after checking starts

		'''
		#Check to see if a file is added to the directory
		added = [f for f in after if not f in before] 
		If a file exist in the list "after", but not in the list "before" it is added to the list  "added"
		'''
		added = [f for f in after if not f in before]

		'''
		Check to see if a file is removed from the directory
		removed = [f for f in before if not f in after]
		If a file exists in the list "before" not in the list after, it is added to the list "removed"
		'''
		removed = [f for f in before if not f in after]
		if added: print( "Added: ", ", ".join (added))
		if removed: print( "Removed: ", ", ".join (removed))
		before = after # Set initial directory state to directory state after change has been made

watchdirectorychange()

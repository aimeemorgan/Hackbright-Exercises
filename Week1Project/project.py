import string
from os import mkdir, listdir, chdir
from shutil import move, rmtree

def reset_files(folder):
	files = get_files(folder)

	for i in files:
		if len(i) == 1:
			path = "./%s" % str(i)
			file_content = get_files(path)
			for i in file_content:
				child_path = './%s/%s' %(path, str(i))
				destination = './files/'
				move(child_path, destination)

			rmtree(path)

def create_dirs():

	for char in string.lowercase:
		path = "./%s" % str(char)
		mkdir(path)

# get directories
def get_files(folder):
	files = listdir(folder)
	return files

# sort files into folder by the first letter
def move_files(files):
	for i in files:
		first_letter = i[0]
		file_to_move = './files/%s' % i
		destination = './%s/' % first_letter 
		move(file_to_move, destination)

def sort_files(folder):
	create_dirs()
	files = get_files(folder)
	move_files(files)

#sort_files('./files')
reset_files('.') # for debugging purpose
import string
from sys import argv

script, filename = argv


def get_text(filename):
	f = open(filename)
	filetext = f.read()
	f.close()
	return filetext

# read file
def read_file(filetext):
	count_dict = {}
	words = remove_punctuation(filetext.lower()).split(" ")

	for word in words:		
		count_dict[word] = count_dict.get(word, 0) + 1
	return count_dict


# word_list = remove_punctuation(word)

def remove_punctuation(filetext):
	clean_text = ''

	for index in range(len(filetext) -1):
		letter = filetext[index]
		space = True
		if not (letter == '-' and (filetext[index + 1] == '-' or filetext[index - 1] == '-')):
			if not (letter == "'" and (filetext[index + 1] == ' ' or filetext[index - 1] == ' ')):
				if letter in string.letters or letter == ' ':
					clean_text += letter
					space = False
		if space:
			clean_text += ' '

	return clean_text

#def print_word_count(count_dict):
#	for word, count in count_dict.iteritems():
#		print word + " " + str(count)

def sort_result_list(count_dict):
	sorted_list = []
	for word, count in count_dict.iteritems():
		sorted_list.append([count, word])
		sorted_list.sort()
		sorted_list.reverse()
	return sorted_list

def print_results(sorted_list):
	for item in sorted_list:
		print item[1], " : ", item[0]


def wordcount(filename):
	filetext = get_text(filename)
	count_dict = read_file(filetext)
	# print_word_count(count_dict)
	sorted_list = sort_result_list(count_dict)
	print_results(sorted_list)

wordcount(filename)
"""Generates a dictionary of words, and beginning segments of words, used in the search algorithm. 

Authors: Thomas Fitzsimmons, J.B. Wincek

"""


import cProfile 
import random
import sys
import dictionary_generator_tester as tester

def remove_shorts(word_list, minimum_length):
	"""Return a list without words shorter than minimum_length."""
	working_word_list = []
	for word in word_list:
		if len(word) >= minimum_length:
			working_word_list.append(word)
	return working_word_list


def quicker_extract_first_letters(word_list, how_long):
	"""slightly optimized: Return the first how_long letters of each word in word_list."""
	working_word_list = []
	for word in word_list:
		if len(word) < how_long:
			pass
		else: 
			working_word_list.append(word[0:how_long])
	return working_word_list

def quicker_build_the_dictionary(word_list, minimum_length, max_length):
	the_dict = {}
	counter = 0
	word_list_without_shorts = remove_shorts(word_list, minimum_length)
	for cur_len in range(1, max_length):
		#print ('Outer entered loop using length:%d' % cur_len) 
		for word in word_list_without_shorts:
			the_dict[word[0:cur_len]] = False
			counter += 1
	print ('Quicker BtD attempted to add a total of %d words. %d words were actually added' % (counter,len(the_dict)))
	return the_dict	



def update_dictionary_entries(word_list, the_dict):
	"""Return a dictionary with values equal to True for keys that are complete words."""
	for word in word_list:
		the_dict[word] = True
	return the_dict

def write_completed_dictionary_to_file(the_dict):
	"""Writes the_dict to usable_dictionary.json in the same folder, creates it if it doesn't exist."""
	try:
		outputLocation = open('usable_dictionary.json','w')
		outputString = str(the_dict)
		outputLocation.write(outputString)
		outputLocation.close()
	except IOError:
		print ("could not open file")

	
def run(which_func, word_list, min_length, max_length):
	"""Run the specified dictionary build with the word list using only the given lengths."""
	
	#some testing functions:
	#word_list = word_list[0:800]
	#word_list = remove_shorts(word_list,3)
	#three_long =  extract_first_letters(word_list,3)
	#print(word_list)
	#print(three_long)
	#print(the_dict)
	the_dict = which_func(word_list, min_length, max_length)
	the_dict = update_dictionary_entries(word_list, the_dict)
	#print the_dict
	write_completed_dictionary_to_file(the_dict)


try:
	file_name = sys.argv[1]
except IndexError:
	file_name = "boggle_dictionary.txt"
try:
	word_list_txt_ob = open(file_name)
except IOError:
	print ('\n\t%s is missing from the current directory.\n\tPlease include a boggle or scrabble dictionary in the same folder as this script\n\tor use the path to one as an argument.' % file_name)
	quit()
word_list_txt = word_list_txt_ob.read()
word_list = word_list_txt.split()

random_sample = tester.extract_a_random_sampling(word_list, 5)




print ( 'random_sample is %d words long and is:\n %s' % (len(random_sample), str(random_sample)))
run(quicker_build_the_dictionary,word_list, 3, 13)
#run(build_the_dictionary,random_sample, 3, 13)


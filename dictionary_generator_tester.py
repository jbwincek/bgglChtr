import cProfile
import random
import sys


def build_the_dictionary(word_list, minimum_length, max_length):
	"""Builds a dictionary containing all the word starts and whole words from the boggle dictionary.
	
	  * The dictionary that is returned has keys for all the complete words in word_list.
	    It  also contains the beginning of every whole word, there are keys for each length,
	    of whole word. 
	  * The meaning of the values of each entry:
	  	* True: the key is a full, complete word. 
	  	* False: the key is some part of a word. 
	"""
	the_dict = {}
	counter = 0 
	word_list_without_shorts = remove_shorts(word_list, minimum_length)
	#print('The length of working_word_list is %d.' % len(word_list_without_shorts))
	#outer loop to add items of each particular length
	for cur_len in range(1, max_length):
		working_word_list = extract_first_letters(word_list_without_shorts, cur_len) 
		for word in working_word_list:
			#print(' %s' % word),
			the_dict[word] = False
			counter += 1
	print ("Regular BtD attempted to add a total of %d words. %d words were actually added" % (counter,len(the_dict)))
	return the_dict


def extract_first_letters(word_list, how_long):
	"""Return the first how_long letters of each word in word_list."""
	working_word_list = []
	for word in word_list:
		if len(word) < how_long:
			pass
		elif len(word) == how_long: 
			working_word_list.append(word)
		else: 
			working_word_list.append(word[0:how_long])
	return working_word_list

def extract_a_random_sampling(word_list, how_many):
	"""Uses for testing purposes.  Return a list containing a specified number of words from the passed list."""
	working_word_list = []
	for i in range(0, how_many):
		working_word_list.append(random.choice(word_list))
	return working_word_list

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

def write_completed_dictionary_to_file(the_dict):
	"""Writes the_dict to usable_dictionary.json in the same folder, creates it if it doesn't exist."""
	try:
		outputLocation = open('usable_dictionary.json','w')
		outputString = str(the_dict)
		outputLocation.write(outputString)
		outputLocation.close()
	except IOError:
		print ("could not open file")

# figure out how long it takes to build the dictionary
#cProfile.run('run(build_the_dictionary,random_sample,3,13)')
#cProfile.run('run(quicker_build_the_dictionary,random_sample,3,13)')


#First letter extraction tests:
#mini_list = ['of','mice','and','women','contemplate','b']
#print( extract_first_letters(mini_list,4))
#print( quicker_extract_first_letters(mini_list,4))

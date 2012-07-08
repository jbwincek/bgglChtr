###########################################################
# Python Relational Letter Hasher Mapper 
# Author: Thomas Fitzsimmons, J.B. Wincek
# 
# This program will read in a large dictionary file
# and go through character by character and count 
# the number of times letters are seen next to each other
# and then store that number in a hash map.
# This hash map will later be used by a boggle solver
# in order to speed up the process in which it finds
# words.
############################################################

import sys

#	Takes in a word_list and runs the commands to create a hash map
#	of relational letters
def word_list_processor(word_list):
	"""Takes in a word_list and runs the commands to create a hash map
		of relational letters"""
	letter_hash_map = {}
	for word in word_list:
		if len(word) >= 4:
			for i in range(len(word)-1):
				add_or_update_word_hash_map(word[i:i+2], letter_hash_map)
	# Sorting the list doesn't quite work. The formatting is off
	#write_completed_hash_map_to_file(sorted(letter_hash_map.items()))
	write_completed_hash_map_to_file(letter_hash_map)
	
	
#	Checks if the two letter relation already exists in the map
#	then either increments it by 1 if it does or adds it			
def add_or_update_word_hash_map(two_chars, letter_hash_map):
	"""Checks if the two letter relation already exists in the map
		then either increments it by 1 if it does or adds it"""
	if two_chars in letter_hash_map:
		letter_hash_map[two_chars] += 1
	else:
		letter_hash_map[two_chars] = 1
	
	
#	Writes letter_hash_map to relational_letters.json 
#	in the same folder, creates it if it doesn't exist.
def write_completed_hash_map_to_file(letter_hash_map):
	"""Writes letter_hash_map to relational_letters.json 
		in the same folder, creates it if it doesn't exist."""
	try:
		outputLocation = open('relational_letters.json','w')
		outputString = str(letter_hash_map)
		outputLocation.write(outputString)
		outputLocation.close()
	except IOError:
		print ("could not open file")
	

# The main function for this program.
# Opens up the dictionary and passes it onto the processor
def run_relational_letters():
	"""The main function for this program. 
		Opens up the dictionary and passes it onto the processor"""
	# import the dictionary file by either the first arg
	# or default to boggle_dictionary.txt
	try:
		file_name = sys.argv[1]
	except IndexError:
		file_name = "boggle_dictionary.txt"
	try:
		word_list_txt_ob = open(file_name)
	except IOError:
		print ("""\n\t%s is missing from the current directory.
		\n\tPlease include a boggle or scrabble dictionary in the 
		same folder as this script
		\n\tor use the path to one as an argument."""
		% file_name)
		quit()

	word_list_txt = word_list_txt_ob.read()
	word_list = word_list_txt.split()
	word_list_processor(word_list)
	
# Run the program
run_relational_letters()
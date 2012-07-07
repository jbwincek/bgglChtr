###########################################################
# bgglChtr: Main Function
# Author: Thomas Fitzsimmons, Jeff Wincek
# 
# This program is the main controller for the program
# bgglChtr. 
############################################################

import sys


# The main function for bgglChtr
def main_function():
	"""The main function for bgglChtr.\n
	Takes in args as follows:\n
	\t filename <depth> <letters in the board as they appear>"""
	
	# Get the depth from the args
	try:
		depth_of_search = sys.argv[1]
	except IndexError:
		depth_of_search = input('Please enter the depth you wish to search: ')
		
	if depth_of_search == None:
		depth_of_search = 5
	
	# add letters to the graph as vectors, create edges between neighbor vectors
	graph_placeHolder = []
	try:
		for i in range(2,18):
			if sys.argv[i].isalpha():
				graph_placeHolder.append(sys.argv[i]);
			else: 
				print("%s is not a character" % sys.argv[i])
	except IndexError:
		print('Please enter 16 character to populate the board:')
		for i in range(1,17):
			chars_good = False
			while not chars_good:
				input_chars = raw_input('%d.) ' % i).strip() #chars is plural because the Qu case
				if input_chars.isalpha() and len(input_chars) <= 2:
					graph_placeHolder.append(input_chars)
					chars_good = True
				else:
					print("'%s' is not valid input. Please enter a either one or two characters" % input_chars)
					chars_good = False
				
		
	# Check that the graph has the correct number of items
	if len(graph_placeHolder) != 16:
		print('There are not 16 items in the graph, exiting...')
		quit()
		
	for index in range(1,len(graph_placeHolder)+1):
		print("%s "% graph_placeHolder[index-1]),
		if index % 4 == 0:
			print('\n'),
	

main_function()
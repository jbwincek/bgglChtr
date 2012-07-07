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
			graph_placeHolder.append(sys.argv[i]);
	except IndexError:
		print('Please enter 16 character to populate the board:')
		for i in range(1,17):
			chars_good = False
			while not chars_good:
				input_chars = raw_input(repr(i) + ') ')
				if isinstance(input_chars, str) and len(input_chars) <= 2 and input_chars != None:
					graph_placeHolder.append(input_chars)
					chars_good = True
				else:
					print('Please enter characters of max length 2')
					chars_good = False
				
		
	# Check that the graph has the correct number of items
	if len(graph_placeHolder) != 16:
		print('There are not 16 items in the graph, exitting...')
		quit()
		
	for char in graph_placeHolder:
		print(char + ", ")
	

main_function()
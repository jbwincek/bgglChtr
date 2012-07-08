"""
###########################################################
# bgglChtr: Main Function
# Authors: Thomas Fitzsimmons, J.B. Wincek
# 
# This program is the main controller for the program
# bgglChtr. 
############################################################
"""

import sys
import Graph
from termcolor import colored 

segmented_dictionary = {}
segmented_dictionary_location = 'usable_dictionary.json'

def brute_force(graph,depth=5):
	for vertex in graph.vertices():
		brute_recurse(graph,vertex,depth,'')
			
def brute_recurse(graph,vertex,depth,word):
	for neighbor in graph.get_neighbors(vertex):
		word = word + neighbor.label
		try: 
			if segmented_dictionary[word]:
				print word
			else:
				if depth > 0:
					brute_recurse(graph,neighbor,depth-1,word)
				else: 
					break
		except KeyError: 
			break 		
			
def load_segmented_dictionary(file_location):
	"""Load the dictionary containing all the words used for the search algorithm."""
	try:
		
		print("Loading segmented dictionary from %s." % file_location)
		inputLocation = open(file_location,'r')
		inputString = inputLocation.read()
		segmented_dictionary = eval(inputString)
		print("Load complete.")
	except IOError:
		print colored('There was an error finding or opening the file.','red')
		quit()

def display_the_board(vertex_holder):
	"""Prints the board in a human readable format resembling the actual board to standard out."""
	for index in range(1,len(vertex_holder)+1):
		print("%s "% vertex_holder[index-1]),
		if index % 4 == 0:
			print('\n'),

def interactive_entry_mode(vertex_holder):
	print('Please enter 16 character to populate the board:')
	for i in range(1,17):
		chars_good = False
		while not chars_good:
			input_chars = raw_input('%d.) ' % i).strip() #chars is plural because the Qu case
			if input_chars.isalpha() and len(input_chars) <= 2:
				vertex_holder.append(Graph.Vertex(input_chars))
				chars_good = True
			else:
				print("'%s' is not valid input. Please enter a either one or two characters" % input_chars)
				chars_good = False
	return vertex_holder		

def build_(vertex_holder):
	"""Return a list of the vertices in order from either the argv or user input
	CHECK: Passing vertex holder to this method may not actually be needed.
	"""
	try:
		for i in range(2,18):
			if sys.argv[i].isalpha():
				vertex_holder.append(Graph.Vertex(sys.argv[i]));
			else: 
				print("%s is not a character" % sys.argv[i])
	except IndexError:
		vertex_holder = interactive_entry_mode(vertex_holder)
		# Check that the graph has the correct number of items
	if len(vertex_holder) != 16:
		print('There are not 16 items in the graph, exiting...')
		quit()
	else: 
		return vertex_holder
		
def get_depth():
	"""Return the depth passed as an argv if available, else prompt the user for the search depth."""
	try:
		depth_of_search = sys.argv[1]
	except IndexError:
		depth_of_search = input('Please enter the depth you wish to search: ')	
	if depth_of_search == None:
		depth_of_search = 5
	return depth_of_search

# The main function for bgglChtr

def main_function():
	"""The main function for bgglChtr
	Takes in args as follows:
		filename <depth> <letters in the board as they appear>"""
	
	vertex_holder = []	
	load_segmented_dictionary(segmented_dictionary_location)
	depth_of_search = get_depth()
	vertext_holder = build_(vertex_holder)
	
	display_the_board(vertex_holder)
	graph_of_letters = Graph.Graph(vertex_holder, [])
	graph_of_letters.find_graph_edges(vertex_holder)
	brute_force(graph_of_letters,depth_of_search)

main_function()
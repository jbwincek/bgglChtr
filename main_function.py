###########################################################
# bgglChtr: Main Function
# Author: Thomas Fitzsimmons, Jeff Wincek
# 
# This program is the main controller for the program
# bgglChtr. 
############################################################

import sys
import Graph

def find_graph_edges(graph_of_letters, vertex_holder):
	for i in range(0,len(vertex_holder)):
		if (i+1) < 16 and ((i+1)%4) != 0:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i+1])
			graph_of_letters.add_edge(e)
		if (i-1) >= 0 and ((i-1)%4) != 3:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i-1])
			graph_of_letters.add_edge(e)
		if (i+3) < 16 and ((i+3)%4) != 3:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i+3])
			graph_of_letters.add_edge(e)
		if (i-3) >= 0 and ((i-3)%4) != 0:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i-3])
			graph_of_letters.add_edge(e)
		if (i+4) < 16:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i+4])
			graph_of_letters.add_edge(e)
		if (i-4) >= 0:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i-4])
			graph_of_letters.add_edge(e)
		if (i+5) < 16 and ((i+5)%4) != 0:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i+5])
			graph_of_letters.add_edge(e)
		if (i-5) >= 0 and ((i-5)%4) != 3:
			e = Graph.Edge(vertex_holder[i], vertex_holder[i-5])
			graph_of_letters.add_edge(e)
			
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
	vertex_holder = []
	try:
		for i in range(2,18):
			if sys.argv[i].isalpha():
				vertex_holder.append(Graph.Vertex(sys.argv[i]));
			else: 
				print("%s is not a character" % sys.argv[i])
	except IndexError:
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
				
	# Check that the graph has the correct number of items
	if len(vertex_holder) != 16:
		print('There are not 16 items in the graph, exiting...')
		quit()
		
	for index in range(1,len(vertex_holder)+1):
		print("%s "% vertex_holder[index-1]),
		if index % 4 == 0:
			print('\n'),
	
	graph_of_letters = Graph.Graph(vertex_holder, [])
	find_graph_edges(graph_of_letters, vertex_holder)
	for i in range(0,len(vertex_holder)):
		print(repr(vertex_holder[i]) + ' = ' + repr(graph_of_letters.out_vertices(vertex_holder[i])))

main_function()
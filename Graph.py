""" Graph class that utilizes Vertex and Edge subclasses. 

Based on the code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html

Authors: Thomas Fitzsimmons, J.B. Wincek

"""

class Vertex(object):
	"""A Vertex is a node in a graph."""

	def __init__(self, label='', visited = False):
		self.label = label
		self.visited = False

	def __repr__(self):
		"""Returns a string representation of this object that can
		be evaluated as a Python expression."""
		return 'Vertex(%s)' % repr(self.label)

	def __str__(self):
		return 'V(%s)' % str(self.label)
	
	def visit():
		self.visited = True
	
	def reset():
		self.visited = False
	
	#def label():
	#	return self.label
		
class Edge(tuple):
	"""An Edge is a list of two vertices."""

	def __new__(cls, *vs):
		"""The Edge constructor takes two vertices."""
		if len(vs) != 2:
			raise ValueError, 'Edges must connect exactly two vertices.'
		return tuple.__new__(cls, vs)

	def __repr__(self):
		"""Return a string representation of this object that can
		be evaluated as a Python expression."""
		return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

	def __str__(self):
		return 'E[%s, %s]' % (repr(self[0]), repr(self[1]))


class Graph(dict):
	"""A Graph is a dictionary of dictionaries.	 The outer
	dictionary maps from a vertex to an inner dictionary.
	The inner dictionary maps from other vertices to edges.
	
	For vertices a and b, graph[a][b] maps
	to the edge that connects a->b, if it exists."""

	def __init__(self, vs=[], es=[]):
		"""Creates a new graph.	 
		vs: list of vertices;
		es: list of edges.
		"""
		for v in vs:
			self.add_vertex(v)
			
		for e in es:
			self.add_edge(e)
	
	def find_graph_edges(self, vertex_holder):
		"""Loop through all the vertices and find edges based on position
			Nodes are laid out like: 
			 0	1  2  3 
			 4	5  6  7
			 8	9 10 11 
			12 13 14 15
			
		"""
		for i in range(0,len(vertex_holder)):
			#Get edges to the right and left
			if (i+1) < 16 and ((i+1)%4) != 0:
				e = Edge(vertex_holder[i], vertex_holder[i+1])
				self.add_edge(e)
			#Get edges diagonally /
			if (i+3) < 16 and ((i+3)%4) != 3:
				e = Edge(vertex_holder[i], vertex_holder[i+3])
				self.add_edge(e)
			#Get edges vertically
			if (i+4) < 16:
				e = Edge(vertex_holder[i], vertex_holder[i+4])
				self.add_edge(e)
			#Get edges diagonally \
			if (i+5) < 16 and ((i+5)%4) != 0:
				e = Edge(vertex_holder[i], vertex_holder[i+5])
				self.add_edge(e)
				
			
	def add_vertex(self, v):
		"""Add a vertex to the graph."""
		self[v] = {}
	
	def get_edge(self, v, w):
		"""Returns the edge between v and w"""
		try:
			return self[v][w]
		except KeyError: 
			return None

	def add_edge(self, e):
		"""Adds and edge to the graph by adding an entry in both directions.

		If there is already an edge connecting these Vertices, the
		new edge replaces it.
		"""
		v, w = e
		self[v][w] = e
		self[w][v] = e

	def remove_edge(self, e):
		"""Removes the edge"""
		v,w = e
		self[v][w] = None
		self[w][v] = None
		
	def vertices(self):
		"""Returns all the vertices in the graph"""
		return self.keys()
	
	def edges(self):
		"""Returns all the edges within a graph. Returns a non-flat list"""
		return_list	 = []
		for key in self.keys():
			return_list.append(self[key].values())
		return return_list
		
	def get_neighbors(self, v):
		"""Returns a list of a vertice's neighbors. Returns a non-flat list"""
		neighbor_list = []
		for neighbor in self[v]:
			neighbor_list.append(neighbor)
		return neighbor_list
			

if __name__ == '__main__':
	import sys
	main(*sys.argv)

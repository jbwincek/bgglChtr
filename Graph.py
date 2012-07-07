""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    def __str__(self):
        return 'V(%s)' % str(self.label)

		
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
    """A Graph is a dictionary of dictionaries.  The outer
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
        return_list  = []
        for key in self.keys():
            return_list.append(self[key].values())
        return return_list
		
    def out_vertices(self, v):
        """Returns a list of a vertice's neighbors. Returns a non-flat list"""
        neighbor_list = []
        for neighbor in self[v]:
            neighbor_list.append(neighbor)
        return neighbor_list
			
def main(script, *args):
    v = Vertex('v')
    # print v
    w = Vertex('w')
    # print w
    y = Vertex('y')
    e = Edge(v, w)
    # print e
    e2 = Edge(y, w)
    g = Graph([v,w], [e])
    g.add_vertex(y)
    # print g
    edge = g.get_edge(v,w)
    g.add_edge(e2)
    # print e2
    # print g
    e3 = g.get_edge(v, w)
    # print e3    
    print g.out_vertices(w)
    print g.out_vertices(v)
    print g.out_vertices(y)

if __name__ == '__main__':
    import sys
    main(*sys.argv)

"""
Contains the parts needed to implement a Breath First Search 

deque is a double ended list 

to simulate a queue:
use the append(x) method to add to the start of the queue
use the popleft() method to return the last item in the queue

"""
from collections import deque 

# the next three functions will compile but they don't work
def searcher(graph,verticies,the_dict):
	for vert in verticies:
		search(graph, vert, the_dict)

def _is_empty(q):
	retval = False
	try: 
		q.pop()
	except IndexError:
		return True
	return retval
	
def search(graph,start,the_dict):
	q = deque() 
	temp_path = [start]
	q.append(temp_path)
	iGotHere = 'made it to the finally block'
	while _is_empty(q) == False:
		try:
			tmp_path = q.popleft()
		except IndexError:
			break
		last_node = tmp_path[len(tmp_path)-1]
		word = ''.join(temp_path)
		print tmp_path
		try:
			if the_dict[word]:
				print "VALID_PATH : ",tmp_path
		finally:
			print iGotHere
			for link_node in graph[last_node]:
				if link_node not in tmp_path:
					new_path = []
					new_path = tmp_path + [link_node]
					q.enqueue(new_path)

#path_queue = MyQUEUE() # now we make a queue
#BFS(graph,"A","D",path_queue)

def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])

# I gave up on this block of code and started trying a new way
def bfs_tester(graph, start, dict):
	
	connections = 0 
	layer = 0 
	#save the values from bfs for later use
	table = []
	for first, second in bfs(graph,start):
		table.append([str(first),str(second)])
		print("%s to %s, connection: %d" % (first,second,connections))
		connections+=1
	# create a list of all the nodes that have children 
	first_list = []
	for entry in table:
		if entry[0] not in first_list:
			first_list.append(entry[0])
	#print first_list
	
	dict_attempt = {}
	for entry in table:
		try:
			dict_attempt[entry[0]].append(entry[1])
		except KeyError:
			dict_attempt[entry[0]] = [entry[1]]
	print dict_attempt
	
	for entry in dict_attempt:
		#print entry,dict_attempt[entry] 
		for sub_entry in dict_attempt[entry]:
			pass

def bfs_tester_v2(graph,start,dict):
	table=[]
	connections = 0 
	dict_attempt = {}
	children_added = []
	parents_added = []
	for first, second in bfs(graph,start):
		first = str(first)
		second = str(second)
		print("%s to %s, connection: %d" % (first,second,connections))
		connections+=1
		try:
			dict_attempt[first].append(second)
		except KeyError:
			dict_attempt[first] = [second]
			parents_added.append(first)
		children_added.append(second)
	children_added = set(children_added)
	print dict_attempt
	print parents_added,children_added


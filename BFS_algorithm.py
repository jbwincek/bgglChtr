"""
Contains the parts needed to implement a Breath First Search 

deque is a double ended list 

to simulate a queue:
use the append(x) method to add to the start of the queue
use the popleft() method to return the last item in the queue

"""
from collections import deque 

def search(graph,start,q,the_dict):
	queue = deque() 
	
	temp_path = [start]
	
	queue.append(temp_path)
	
	while q.IsEmpty() == False:
		tmp_path = queue.popleft()
		last_node = tmp_path[len(tmp_path)-1]
		word = ''.join(temp_path)
		print tmp_path
		try:
			if the_dict[word]:
				print "VALID_PATH : ",tmp_path
		finally:
			for link_node in graph[last_node]:
				if link_node not in tmp_path:
					new_path = []
					new_path = tmp_path + [link_node]
					q.enqueue(new_path)

#path_queue = MyQUEUE() # now we make a queue
#BFS(graph,"A","D",path_queue)

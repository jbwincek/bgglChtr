import cProfile 

def remove_shorts(word_list,minimum_length):
	"""Remove words shorter than minimum_length, return the modified list."""
	working_list = []
	for word in word_list:
		if len(word) >= minimum_length:
			working_list.append(word)
	return working_list

def extract_first_letters(word_list,how_long):
	"""Return the first how_long letters of each word in word_list."""
	working_list = []
	for word in word_list:
		if len(word) < how_long:
			pass
		elif len(word) == how_long: 
			working_list.append(word)
		else: 
			working_list.append(word[0:how_long])
	return working_list

def quicker_extract_first_letters(word_list,how_long):
	"""slightly optimized: Return the first how_long letters of each word in word_list."""
	working_list = []
	for word in word_list:
		if len(word) < how_long:
			pass
		else: 
			working_list.append(word[0:how_long])
	return working_list

def build_the_dictionary(word_list,minimum_length,max_length):
	the_dict = {}
	counter = 0 
	list_without_shorts = remove_shorts(word_list,minimum_length)
	#print('The length of working_list is %d.' % len(list_without_shorts))
	#outer loop to add items of each particular length
	for cur_len in range(1,max_length):
		working_list = extract_first_letters(list_without_shorts,cur_len) 
		for word in working_list:
			#print(' %s' % word),
			the_dict[word]=False
			counter += 1
	print ('Added a total of %d words.' % counter)
	return the_dict

def quicker_build_the_dictionary(word_list,minimum_length,max_length):
	the_dict = {}
	counter = 0
	list_without_shorts = remove_shorts(word_list,minimum_length)
	for cur_len in range(1,max_length):
		#print ('Outer entered loop using length:%d' % cur_len) 
		for word in list_without_shorts:
			the_dict[word[0:cur_len]] = False
			counter+=1
	print ('Added a total of %d words.' % counter)
	return the_dict	

def extract_a_random_sampling(word_list,how_many)

def run(where,min_length,max_length):
	word_list_txt_ob = open(where)
	word_list_txt = word_list_txt_ob.read()
	word_list = word_list_txt.split()
	#word_list = word_list[0:800]
	#word_list = remove_shorts(word_list,3)
	#three_long =  extract_first_letters(word_list,3)
	#print(word_list)
	#print(three_long)
	#print(the_dict)
	the_dict = build_the_dictionary(word_list,min_length,max_length)
	
cProfile.run('run("boggle_dictionary.txt",3,13)')
#run("boggle_dictionary.txt",3,13)



#First letter extraction tests
#mini_list = ['of','mice','and','women','contemplate','b']
#print( extract_first_letters(mini_list,4))
#print( quicker_extract_first_letters(mini_list,4))

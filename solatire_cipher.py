def str_to_alpha(s):
	"""Cleans a string to have only alphanumeric chars.
	
	Args:
	    s (str): string to be cleaned
	
	Returns:
	    str: cleaned string containing only alphanumeric
	"""
	ns = str()
	for letter in s:
		if letter.isalpha():
			ns += letter
	return ns

def str_to_four(s):
	"""Splits string into 4 groups of 5 chars.
	
	Args:
	    s (str): String to be split.
	
	Returns:
	    str: String split into 4 groups of 5 chars separated by ' '.
	"""
	ns = str()
	for count, letter in enumerate(s,1):
		ns += letter
		if count % 5 == 0:
			# Every 5 letters, add space
			ns += ' '
	return ns

def str_to_numbered_dict(s):
	"""Pair each char of a string to a number which increments starting at 1.
	
	Args:
	    s (str): Pair str with numbers.
	
	Returns:
	    dict: Dictionary with each char of param paired with numbers.
	"""
	ndict = dict()

	for count, letter in enumerate(s,1):
		ndict[letter] = count

	return ndict

def str_to_num_using_key(s, key):
	"""Turn string into a series of numbers based on provided key dictionary.
	
	Args:
	    s (str): String to be converted into numbers.
	    key (dict): Dictionary that pairs each alpha to a number. 
	
	Returns:
	    list: List of numbers from converted string.
	"""
	nums = list()
	for letter in s:
		if letter.isalpha():
			nums.append(key[letter])
	return nums

def merge_lists(l1, l2):
	"""
	Merges each index of param1 and param2 to create a new list. If merged indexes are greater than 26, subtract 26.
	
	Args:
	    l1 (list): list of numbers.
	    l2 (list): list of numbers.
	
	Returns:
	    list: List of combined indexes of l1 & l2.
	"""
	mylist = list()
	for i, j in zip(l1, l2):
		temp = i + j
		if temp > 26:
			temp = temp-26
		mylist.append(temp)

	return mylist

def value_to_key(v, mydict):
	"""Iterate through dictionary until matched value is matched.
	
	Args:
	    v (int): Value to use.
	    mydict (dict): Dictionary provided.
	
	Returns:
	    key: Return key of provided value.
	"""
	for key in mydict:
		if mydict[key] == v:
			return key

def num_list_to_string(nums, key):
	"""Convert numbers into string using provided key.
	
	Args:
	    nums (list): List of numbers.
	    key (dict): Dictionary pairing alphabet to numbers.
	
	Returns:
	    str: A alphanumeric string converted using provided key.
	"""
	s = str()
	for n in nums:
		s += value_to_key(n, key)
	return s

def str_to_nums(s, key):
	"""
	Take a string and convert to uppercase, remve non-alphanumeric characters, split into 4 groups of 5 chars, and convert into numbers using provided dictionary key.
	
	Args:
	    s (str): Description
	    key (dict): Dictionary provided to convert alpha -> numeric using key, values
	
	Returns:
	    list: A list of nums converted from string.
	"""
	s = s.upper()	 
	s = str_to_alpha(s)
	s = str_to_four(s) # I don't think I need this until end.
	s = str_to_num_using_key(s, key)
	return s

abc = 'abcdefghijklmnopqrstuvwxyz'.upper()
abckey = str_to_numbered_dict(abc)

s1 = 'Code in Ruby, live longer!'
s1 = str_to_nums(s1, abckey)

keystream = 'DWJXH YRFDG TMSHP UURXJ'
s2 = str_to_nums(keystream, abckey)

merged = merge_lists(s1,s2)
s = num_list_to_string(merged, abckey)
print str_to_four(s)
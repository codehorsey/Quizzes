def return_alpha(s):
	ns = str()
	for letter in s:
		if letter.isalpha():
			ns += letter
	return ns

def split_into_4(s):
	ns = str()
	for count, letter in enumerate(s,1):
		ns += letter
		if count % 5 == 0:
			# Every 5 letters, add space
			ns += ' '
	return ns

def string_into_numerical_dict(s):
	ndict = dict()

	for count, letter in enumerate(s,1):
		ndict[letter] = count

	return ndict

def convert_str_to_num_using_key(s, key):
	nums = list()
	for letter in s:
		if letter.isalpha():
			nums.append(key[letter])
	return nums

def convert_num_to_str_using_key(nums, key):
	s = str()
	for n in nums:
		if n.isdigit():
			print key[n]
			s += key[n]


def merge_lists(s, s2):
	mylist = list()
	for i, j in zip(s, s2):
		temp = i + j
		if temp > 26:
			temp = temp-26
		mylist.append(temp)

	return mylist
	
def return_numbers_into_str(nums):
	for n in nums:
		lookup_key_with_value(n, abckey)


def lookup_key_with_value(n, mydict):
	for key in mydict:
		if mydict[key] == n:
			return key
def convert_merged_lists_into_one_string(merged, abckey):
	s = str()
	for n in merged:
		s += lookup_key_with_value(n, abckey)
	return s

def str_to_nums(s, key):
	s = s.upper()	 
	s = return_alpha(s)
	s = split_into_4(s)
	s = convert_str_to_num_using_key(s, key)
	return s

abc = 'abcdefghijklmnopqrstuvwxyz'.upper()
abckey = string_into_numerical_dict(abc)

s = 'Code in Ruby, live longer!'
s = str_to_nums(s, abckey)

keystream = 'DWJXH YRFDG TMSHP UURXJ'
s2 =  str_to_nums(keystream, abckey)

merged = merge_lists(s,s2)
s = convert_merged_lists_into_one_string(merged, abckey)
print split_into_4(s)
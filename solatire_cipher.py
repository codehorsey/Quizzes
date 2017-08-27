

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

def app(s, key):
	s = s.upper()	 
	s = return_alpha(s)
	s = split_into_4(s)
	s = convert_str_to_num_using_key(s, key)
	return s


abc = 'abcdefghijklmnopqrstuvwxyz'.upper()
abckey = string_into_numerical_dict(abc)

s = 'Code in Ruby, live longer!'
s = app(s, abckey)

keystream = 'DWJXH YRFDG TMSHP UURXJ'
s2 =  app(keystream, abckey)


for i, j in zip(s, s2):
	temp = i + j
	if temp > 26:
		temp = temp-26
	print temp
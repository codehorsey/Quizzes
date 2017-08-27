
s = 'Code in Ruby, live longer!'
print s
s = s.upper()
print 
n = ''
for letter in s:
	if letter.isalpha():
		n += letter

print n
def split_into_4(s):
	new_str = str()
	for count, letter in enumerate(s,1):
		print letter, count
		if count % 5 == 0:
			# Every 5 letters, add space
			new_str += letter
			new_str += ' '
		else:
			new_str += letter

	return new_str

print split_into_4(n)
n = split_into_4(n)
abc = 'abcdefghijklmnopqrstuvwxyz'.upper()
thedict = {}

for count, letter in enumerate(abc,1):
	thedict[letter] = count

print thedict
print thedict['A']
def convert_to_nums(s, cipher):
	nums = str()
	for letter in s:
		if letter.isalpha():
			nums += str(cipher[letter])
			nums += ' '

	return nums

keystream = 'DWJXH YRFDG TMSHP UURXJ'
anum = convert_to_nums(n, thedict)
bnum = convert_to_nums(keystream, thedict)

print anum
print bnum
print anum.split()
print bnum.split()
for n in bnum.split():
	print type(n)

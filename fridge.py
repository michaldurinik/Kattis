import sys
word = sys.stdin.readline()
word = word.strip()
string_list = []
num_list = [0]*10

for s in str(word):
	string_list.append(int(s))

string_list = sorted(string_list)

for l in string_list:
	num_list[l] += 1

found = False
i = 1
while i < 10:
	if num_list[i] == 0:
		print(i)
		found = i
		break
	i += 1 

if not found:
	lowest = num_list[1]
	index = 1
	i = 1
	while i < 10:
		if num_list[i] < lowest:
			lowest = num_list[i]
			index = i
		i += 1
	if num_list[0] < num_list[index]:
		print(str(index)+ ('0'*(num_list[0]+1)))
	else:
		print((num_list[index]+1)*str(index))
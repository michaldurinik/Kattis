import sys

def finds(list, word):
	for w in list:
		if len(word) >= len(w):
		    if word[-len(w):] == w:
			    return True
		
	return False
list1 =[]
list2=[]
word = sys.stdin.readline()
word2 = word.strip()
int1 = input()

i = 0
while i < int(int1):
	line = sys.stdin.readline()
	words = line.strip().split()
	if finds(words, word2):
		list1.append(words)
	i += 1

int2 = input()
i = 0
while i < int(int2):
    if list1 == []:
        print("NO")
    else:
        line = sys.stdin.readline()
        words = line.split()
        word = words[-1].strip()
        output = "NO"
        for l in list1:
    	    if finds(l, word):
    		    output = "YES"
        print('{:s}'.format(output))
    i += 1
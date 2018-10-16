#https://open.kattis.com/problems/anewalphabet
from sys import stdin

dictionary = {
"a":"@",
"b":"8",
"c":"(",
"d":"|)",
"e":"3",
"f":"#",
"g":"6",
"h":"[-]",
"i":"|",
"j":"_|",
"k":"|<",
"l":"1",
"m":"[]\/[]",
"n":"[]\[]",
"o":"0",
"p":"|D",
"q":"(,)",
"r":"|Z",
"s":"$",
"t":"']['",
"u":"|_|",
"v":"\/",
"w":"\/\/",
"x":"}{",
"y":"`/",
"z":"2",
}

text = stdin.readline().strip()
translated = ""
for c in text:
	if c.lower() in dictionary:
		translated += dictionary[c.lower()]
	else:
		translated += c

print(translated)

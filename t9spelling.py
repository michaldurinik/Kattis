#https://open.kattis.com/problems/t9spelling
from sys import stdin

t9_dict = {"a":"2", "b":"22", "c":"222","d":"3", "e":"33", "f":"333", "g":"4", "h":"44", "i":"444", "j":"5", "k":"55", "l":"555", "m":"6", "n":"66", "o":"666", "p":"7", "q":"77", "r":"777", "s":"7777", "t":"8", "u":"88", "v":"888", "w":"9", "x":"99", "y":"999", "z":"9999", " ":"0"}

no_cases = int(stdin.readline().strip())

for i in range(1, no_cases + 1):
    #inputline without \n, strip() wouldremoves all spaces
    text = stdin.readline()[:-1]

    prev = " "
    lst = []

    for c in text:
        digits = t9_dict[c]

        #space if previous letter and current are in same group
        if prev == digits[0]:
             lst.append(" ")  

        lst.append(t9_dict[c])
        prev = digits[0]

    print("Case #" + str(i) + ": " + "".join(lst))


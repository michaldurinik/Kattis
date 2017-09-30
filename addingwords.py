#https://open.kattis.com/problems/addingwords
from sys import stdin
pairs_dict = {}

for line in stdin:
    line = line.strip()

    if line == "clear":
        pairs_dict = {}
        continue

    definition, *printable_lst = line.split()

    if definition == "def":
        var_name = printable_lst[0]
        num = int(printable_lst[1])

        if var_name in pairs_dict:
            old_num = pairs_dict[var_name]
            del pairs_dict[old_num]

        pairs_dict[var_name] = num
        pairs_dict[num] = var_name
    else:
        name, *calculations, eq_sign = printable_lst

        found = True
        if name in pairs_dict:
            total = int(pairs_dict[name])
        else:
            found = False
        
        for sign, var in zip(calculations[0::2], calculations[1::2]):
            try:
                if sign == "+":
                    total += pairs_dict[var]
                else:
                    total -= pairs_dict[var]
            except:
                found = False
                break 
  
        if found and total in pairs_dict:
            printable_lst.append(pairs_dict[total])
        else:
            printable_lst.append("unknown")
        print(" ".join(printable_lst))

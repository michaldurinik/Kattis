import sys
for line in sys.stdin:
    line = [int(num) for num in line.strip().split()]
    
    #when file finish with 0 0, it is end of file
    if line[0] == 0 and line[1] == 0:
        break      
    else:
        hated = line[1]
        
        #if there is no hated pair, we only need 1 committee
        if hated == 0:
            print(1)             
        else: 

            hated_pairs = set()
            added_names = set()
            team_dict = {}
            
            i = 0
            while i < hated:
                line = sys.stdin.readline().strip().split()
                name1, name2 = line 
                
                #adding tumples of hated pairs to set
                hated_pairs.add((name1, name2))
                
                i += 1
            for name1, name2 in hated_pairs:
                if not team_dict:
                    team_dict[1] = {name1}
                    team_dict[2] = {name2}
                    added_names.add(name1)
                    added_names.add(name2)
                    #print(team_dict)
                    
                else:
                    for name in name1,name2:
                        print("------------------")
                        #print("name: ", name)
                        recorded = False
                        if name not in added_names: 
                            
                            for team in team_dict.values():
                                
                                if not recorded:
                                    #print("team: ", team)
                                    for person in team:
                                        print("person: ", person)
                                        print("name: ",name)
                                        
                                        if (name, person) in hated_pairs or (person, name)in hated_pairs:
                                            print((name, person))
                                            print(added_names)
                                            print(team_dict)
                                            
                                            break
                                        else:
                                            print("!!!!")
                                            team.add(name)
                                            added_names.add(name)
                                            recorded = True
                                            print(team_dict)
                                            break
                                else:
                                    break
                                
                            if not recorded:
                                    print("#####")
                                    team_dict[len(team_dict)+1] = {name}
                                    added_names.add(name)
                                    print(team_dict)
                                    print("-----------")
                            else:
                                    
                                print(team_dict)
                                print("-----------")
                            
            print(len(team_dict))
            print(team_dict)
            print(hated_pairs)
            print(added_names)

                    
                    
"""               
found = False    
for lst in name_list:
    if name1 in lst[1]:
        found = True
        break
    else:
        lst.append(name1)
        break                        
    
found = False    
for lst in enumerate name_list:
    if name2 in lst:
        found = True
        break
    else:
        lst.append(name1)
        break               

if not found:
    name_list.append([name1])
                    
    name_list.append(name1)
if name2 not in name_list: 
    name_list.append(name2)
"""                    
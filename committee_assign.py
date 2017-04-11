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
            added_names = set()
            team_dict = {}
            hated_pairs = set()
            
            i = 0
            while i < hated:
                line = sys.stdin.readline().strip().split()
                name1, name2 = line 
                
                #adding tumples of hated pairs to set
                hated_pairs.add((name1, name2))
                
                #adding all seen names to set

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
                i += 1
            
            for name1, name2 in hated_pairs:
                if not team_dict:
                    team_dict[1] = {name1}
                    team_dict[2] = {name2}
                    added_names.add(name1)
                    added_names.add(name2)
                    
                else:
                    for name in name1,name2:
                        recorded = False
                        if name not in added_names: 
                            
                            for team in team_dict.values():
                            
                                if not recorded:
                                    for person in team:
                                        if (person, name) or (name, person) in hated_pairs:
                                            break
                                        else:
                                            team.add(name)
                                            recorded = True
                                            break
                                else:
                                    break
                                
                            if not recorded:
                                team_dict[len(team_dict)+1] = {name}
                            
            print(team_dict)        
                    
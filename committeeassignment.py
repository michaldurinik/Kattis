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
            
            people = {}
            hated_pairs = set()
            #added_names = set()
            team_dict = {}
            
            i = 0
            while i < hated:
                line = sys.stdin.readline().strip().split()
                name1, name2 = line 
                
                #adding tumples of hated pairs to set
                hated_pairs.add((name1, name2))
                
                for name in name1,name2:
                    if name not in people:
                        people[name] = 1
                    else:
                        people[name] += 1
                
                i += 1
            for name, frequency in sorted(people.items(), key=lambda x: x[1], reverse=True):
                #print(name, frequency)

                if not team_dict:
                    team_dict[1] = {name}
                    
                else:        
                        recorded = False
                        for team in team_dict.values():
                            found = False
                            
                            if not recorded:
                                for person in team:  
                                
                                    if (name, person) in hated_pairs or (person, name)in hated_pairs:
                                        found = True
                                        break
                                        
                                if not found:
                                   
                                    #print("!!!!")
                                    team.add(name)
                                    recorded = True
                                    break
                            else:
                                break
                            
                        if not recorded:
                                team_dict[len(team_dict)+1] = {name}
                            
            print(len(team_dict))
            #print(team_dict)
            #print(hated_pairs)
            #print(added_names)
                   
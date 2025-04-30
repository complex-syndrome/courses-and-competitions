with open("input.txt", "r") as f:
    line = f.readlines()
    line = [l.strip() for l in line]
    seperate = line.index('')
    
    page_ordering_rules = line[:seperate]
    page_update_number = line[seperate+1:]

    answer1 = 0
    incorrect_list = []
    
    for num in page_update_number:
        valid = True
        n_list = num.split(",")
        
        for i in range(1, len(n_list)):
            for n in range(len(n_list) - i):
                for rule in page_ordering_rules:
                    start, end = rule.split('|')
                    
                    if n_list[n] == end and n_list[n+i] == start:
                        valid = False
                        incorrect_list.append(n_list)
                        break
                if not valid:
                    break
            if not valid:
                break
    
        if valid:
            answer1 += int(n_list[len(n_list) // 2])
            
    answer2 = 0
    for seq in incorrect_list:
        valid = False
        
        while not valid:
            valid = True  
            
            for i in range(len(seq) - 1):  
                for rule in page_ordering_rules:
                    start, end = rule.split('|')
                    
                    if seq[i] == start and seq[i + 1] == end:
                        seq[i], seq[i + 1] = seq[i + 1], seq[i]
                        valid = False  
                        break

        answer2 += int(seq[len(seq) // 2])

print(answer1)
print(answer2)

                
    
    
            
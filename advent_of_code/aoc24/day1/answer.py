with open("input.txt", 'r') as f:
    delim = "   "
    list_a, list_b = map(sorted, zip(*([int(i) for i in line.strip().split(delim)] for line in f)))
    answer1 = sum(abs(a - b) for a, b in zip(list_a, list_b))
    
    answer2 = sum([a*list_b.count(a) for a in list_a])
    
print(answer1)
print(answer2)
def safe(lv):
    return (lv == sorted(lv) or lv == sorted(lv, reverse=True)) and \
        all(1 <= abs(lv[i+1] - lv[i]) <= 3 for i in range(len(lv) - 1))
    
with open("input.txt", "r") as f:
    line = f.readlines()
    arr = [list(map(int, l.strip().split())) for l in line]
    
    answer1 = sum(safe(i) for i in arr)
    
                
    answer2 = 0
    for levels in arr:
        if safe(levels):
            answer2 += 1
            
        else:
            for i in range(len(levels)):
                new = levels[:i] + levels[i+1:]
                if safe(new):
                    answer2 += 1
                    break
    
print(answer1)
print(answer2)


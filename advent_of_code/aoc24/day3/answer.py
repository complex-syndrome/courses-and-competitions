import re

with open("input.txt", "r") as f:
    line = f.readlines()

    matches = re.findall(r"mul\(\d+,\d+\)", "".join(line))
    # format should be mul(50,30)
    
    answer1 = 0
    
    for i in matches:
        a, b = i[4:].split(',')
        b = b[:-1]
        answer1 += int(a)*int(b)
    print(answer1)
    
    matches2 = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", "".join(line))
    answer2 = 0
    add_flag = True
    for i in matches2:
        if i == "do()":
            add_flag = True
        elif i == "don't()":
            add_flag = False
        else:
            if add_flag:
                a, b = i[4:].split(',')
                b = b[:-1]
                answer2 += int(a)*int(b)
                
    print(answer2)
from itertools import product

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    
    op = ["+", "*", "||"]
    
    answer = 0
    for line in lines:
        target, variables = line.split(": ")
        target = int(target)
        
        variables = variables.split()
        operator_count = len(variables) - 1
        
        perm = list(product(op, repeat=operator_count))
        
        for p in perm:
            current_result = int(variables[0])  
            
            for i, operator in enumerate(p):
                next_number = int(variables[i + 1])
                if operator == "+":
                    current_result += next_number
                elif operator == "*":
                    current_result *= next_number
                elif operator == "||": # answer 2
                    current_result = int(str(current_result) + str(next_number))
            
            if current_result == target:
                answer += target
                break
        print("doing sth...")
        
print(answer)
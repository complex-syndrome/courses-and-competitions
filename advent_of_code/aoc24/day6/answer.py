# for 1 gold star

with open("i.txt", "r") as f:
    line = f.readlines()
    matrix = [list(l.strip()) for l in line]

    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    cor = ()
    direction = ''

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col in directions:
                cor = (i, j)
                direction = col
                break
        if cor:
            break

    print("Starting position:", cor)
    print("Starting direction:", direction)

    distinct = {cor}
    
    while True:
        dx, dy = directions[direction]
        x, y = cor[0] + dx, cor[1] + dy
        
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
            break

        if matrix[x][y] == '#':
            if direction == '^':
                direction = '>'
            elif direction == '>':
                direction = 'v'
            elif direction == 'v':
                direction = '<'
            elif direction == '<':
                direction = '^'
        else:
            cor = (x, y)
            distinct.add(cor)
        
        answer1 = len(distinct)
        
    
    x, y = cor
    obstacles = []
    while not (x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0])):
        path_traversed = 0
        
        dx, dy = directions[direction]
        obstacle = x+dx, y+dy
        new_cor = cor
        
        if direction == '^':
            direction = '>'
        elif direction == '>':
            direction = 'v'
        elif direction == 'v':
            direction = '<'
        elif direction == '<':
            direction = '^'
        
        while path_traversed < len(matrix) * len(matrix[0]):
            if cor == new_cor:
                obstacles.append(obstacle)
                
            path_traversed += 1

print(answer1)




        
    
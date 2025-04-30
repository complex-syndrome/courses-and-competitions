with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    answer1 = 0

    rows = len(lines)
    cols = len(lines[0])

    targets = ["XMAS", "SAMX"]

    def count_matches(string, target):
        count = 0
        for i in range(len(string) - len(target) + 1):
            if string[i:i + len(target)] == target:
                count += 1
        return count

    for x in range(rows):
        answer1 += count_matches(lines[x], "XMAS")
        answer1 += count_matches(lines[x], "SAMX")

        for y in range(cols):
            if x + 3 < rows:  
                vertical_word = lines[x][y] + lines[x+1][y] + lines[x+2][y] + lines[x+3][y]
                if vertical_word in targets:
                    answer1 += 1

    for x in range(rows):
        for y in range(cols):
            if x + 3 < rows and y + 3 < cols:
                diagonal_word = (
                    lines[x][y]
                    + lines[x+1][y+1]
                    + lines[x+2][y+2]
                    + lines[x+3][y+3]
                )
                if diagonal_word in targets:
                    answer1 += 1

            if x + 3 < rows and y - 3 >= 0:
                diagonal_word = (
                    lines[x][y]
                    + lines[x+1][y-1]
                    + lines[x+2][y-2]
                    + lines[x+3][y-3]
                )
                if diagonal_word in targets:
                    answer1 += 1

    answer2 = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if lines[x][y] == 'A':
                if lines[x-1][y-1] == lines[x-1][y+1] == 'M' and lines[x+1][y-1] == lines[x+1][y+1] == 'S':
                    answer2 += 1 # topdown
                    
                if lines[x-1][y-1] == lines[x-1][y+1] == 'S' and lines[x+1][y-1] == lines[x+1][y+1] == 'M':
                    answer2 += 1 # downtop
                    
                if lines[x-1][y-1] == lines[x+1][y-1] == 'M' and lines[x-1][y+1] == lines[x+1][y+1] == 'S':
                    answer2 += 1 # leftright
                    
                if lines[x-1][y-1] == lines[x+1][y-1] == 'S' and lines[x-1][y+1] == lines[x+1][y+1] == 'M':
                    answer2 += 1 # rightleft
                    

print(answer1)
print(answer2)

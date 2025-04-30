# Not the correct answer

from itertools import combinations

with open("i.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

antenna = {}

# Get all antenna coordinates
for i, row in enumerate(lines):
    for j, val in enumerate(row):
        if val != '.':
            if val not in antenna:
                antenna[val] = []
            antenna[val].append((i, j))

answer1 = set()

for freq, coords in antenna.items():
    for comba, combb in combinations(coords, 2):
        c1, c2 = sorted([comba, combb])
        x1, y1 = c1
        x2, y2 = c2
        
        dx = x1 - x2
        dy = y1 - y2

        # Calculate antinodes
        ax1, ay1 = (x1 - dx), (y1 - dy)
        ax2, ay2 = (x2 + dx), (y2 + dy)

        # Check bounds and add to the set
        if 0 <= ax1 < len(lines) and 0 <= ay1 < len(lines[0]):
            answer1.add((ax1, ay1))
        if 0 <= ax2 < len(lines) and 0 <= ay2 < len(lines[0]):
            answer1.add((ax2, ay2))

print(list(sorted(answer1)))
print(len(answer1))

# For one gold star

with open("day9/input.txt", "r") as f:
    line = f.read().strip()
    
data = []
idx = 0
i = 0

while i < len(line) - 1:
    length = int(line[i])
    dots = int(line[i + 1])
    
    data += [idx] * length + ['.'] * dots
    i += 2
    idx += 1

if i < len(line):
    data += [idx] * int(line[i])


fptr, bptr = 0, len(data) - 1
while bptr > fptr:
    while fptr < len(data) and data[fptr] != ".":
        fptr += 1
    
    while bptr > fptr and data[bptr] == ".":
        bptr -= 1
    
    if fptr < bptr:
        data[fptr], data[bptr] = data[bptr], "."
        fptr += 1
        bptr -= 1

ans1 = sum(i * val for i, val in enumerate(data) if val != ".")
print(ans1)

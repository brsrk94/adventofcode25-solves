with open('input.txt') as f: lines = [l.strip('\n') for l in f]
w = max(len(l) for l in lines)
lines = [l.ljust(w) for l in lines]
blocks, start, found = [], 0, False
for c in range(w):
    if any(l[c] != ' ' for l in lines):
        if not found: start, found = c, True
    elif found: blocks.append((start, c - 1)); found = False
if found: blocks.append((start, w - 1))
p1 = p2 = 0
for s, e in blocks:
    op = lines[-1][s:e+1].strip()[0]
    #part1
    nums = [int(lines[i][s:e+1]) for i in range(len(lines)-1) if lines[i][s:e+1].strip()]
    res = nums[0]
    for n in nums[1:]: res = res + n if op == '+' else res * n
    p1 += res
    #part2
    nums = []
    for c in range(e, s - 1, -1):
        d = "".join(lines[i][c] for i in range(len(lines)-1) if lines[i][c].isdigit())
        if d: nums.append(int(d))
    res = nums[0]
    for n in nums[1:]: res = res + n if op == '+' else res * n
    p2 += res
print(p1)
print(p2)

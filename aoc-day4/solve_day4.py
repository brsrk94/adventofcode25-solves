grid = [list(l) for l in open('input.txt').read().splitlines()]
H, W = len(grid), len(grid[0])
part1, total = 0, 0

while True:
    rem = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '@':
                if sum(0<=r+i<H and 0<=c+j<W and grid[r+i][c+j]=='@' 
                       for i in (-1,0,1) for j in (-1,0,1)) < 5:
                    rem.append((r,c))
    
    if not rem: break
    if total == 0: part1 = len(rem)
    total += len(rem)
    for r,c in rem: grid[r][c] = '.'

print(f"Part 1: {part1}")
print(f"Part 2: {total}")

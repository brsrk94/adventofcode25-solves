
def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    # Part 1
    pos = 50
    count1 = 0
    for line in lines:
        line = line.strip()
        if not line: continue
        direction = line[0]
        dist = int(line[1:])
        
        if direction == 'R':
            pos = (pos + dist) % 100
        elif direction == 'L':
            pos = (pos - dist) % 100
            
        if pos == 0:
            count1 += 1
            
    print(f"Part 1: {count1}")

    # Part 2
    pos = 50
    count2 = 0
    for line in lines:
        line = line.strip()
        if not line: continue
        direction = line[0]
        dist = int(line[1:])
        
        if direction == 'R':
            hits = (pos + dist) // 100 - pos // 100
            count2 += hits
            pos = (pos + dist) % 100
        elif direction == 'L':
            hits = (pos - 1) // 100 - (pos - dist - 1) // 100
            count2 += hits
            pos = (pos - dist) % 100
            
    print(f"Part 2: {count2}")

if __name__ == '__main__':
    solve()

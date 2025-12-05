with open('input.txt') as f:
    lines = [line.strip() for line in f]

blank_idx = lines.index('')
ranges = [tuple(map(int, line.split('-'))) for line in lines[:blank_idx]]
ingredients = [int(line) for line in lines[blank_idx+1:]]

# Part 1
fresh_count = sum(any(s <= i <= e for s, e in ranges) for i in ingredients)
print(f"Part 1: {fresh_count}")

# Part 2
merged = []
for start, end in sorted(ranges):
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

print(f"Part 2: {sum(e - s + 1 for s, e in merged)}")

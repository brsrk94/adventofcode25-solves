# Part 1
def is_invalid_part1(n):
    s = str(n)
    return len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:] and s[0] != '0'

# Part 2
def is_invalid_part2(n):
    s = str(n)
    if s[0] == '0':
        return False
    for pattern_len in range(1, len(s)):
        if len(s) % pattern_len == 0:
            repeats = len(s) // pattern_len
            if repeats >= 2:
                pattern = s[:pattern_len]
                if pattern * repeats == s:
                    return True
    return False

# Read input
data = open('input.txt').read().strip().split(',')
ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in data]

# Part 1
count1 = sum(n for start, end in ranges for n in range(start, end + 1) if is_invalid_part1(n))

# Part 2
count2 = sum(n for start, end in ranges for n in range(start, end + 1) if is_invalid_part2(n))

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")

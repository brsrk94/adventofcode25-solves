
def solve(k):
    total = 0
    with open('input.txt') as f:
        for line in f:
            digits = [int(c) for c in line.strip() if c.isdigit()]
            if len(digits) < k: continue
            
            current_pos = 0
            num = 0
            for rem in range(k, 0, -1):
                window = digits[current_pos : len(digits) - rem + 1]
                best_digit = max(window)
                offset = window.index(best_digit)
                current_pos += offset + 1
                num = num * 10 + best_digit
            total += num
    return total

# Part 1: Find max joltage with 2 batteries
print(f"Part 1: {solve(2)}") 

# Part 2: Find max joltage with 12 batteries
print(f"Part 2: {solve(12)}")

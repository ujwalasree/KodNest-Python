# Read how many numbers will be entered
number_cnt = int(input())

# Initialize the counters and total
pos_count = 0
neg_count = 0
zero_count = 0
total = 0

# Read and analyze each number
for _ in range(number_cnt):
    num = int(input())
    total += num
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1

# Display the final analysis
print(f"Positive Count: {pos_count}")
print(f"Negative Count: {neg_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")
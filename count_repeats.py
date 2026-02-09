nums = [1, 2, 3, 2, 4, 3, 2]

counts = {}

for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(counts)

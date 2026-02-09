def count_elements(nums):
    if not nums:
        return {}, 0, 0  # counts, unique_count, repeated_count

    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    unique_count = sum(1 for v in counts.values() if v == 1)
    repeated_count = sum(1 for v in counts.values() if v > 1_


def find_max_min(nums):
    max_value = nums[0]
    min_value = nums[0]
    max_index = 0
    min_index = 0

    for i in range(1, len(nums)):
        if nums[i] > max_value:
            max_value = nums[i]
            max_index = i
        if nums[i] < min_value:
            min_value = nums[i]
            min_index = i

    return max_value, max_index, min_value, min_index


nums = [3, 7, 1, 9, 2, 8]
print(find_max_min(nums))

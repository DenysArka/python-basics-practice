def analyze_list(nums):
    print("List analysis:")
    print("-" * 30)

    total_sum = 0
    max_value = nums[0]
    max_index = 0

    for index, value in enumerate(nums):
        total_sum += value

        if value > max_value:
            max_value = value
            max_index = index

        index_type = "even" if index % 2 == 0 else "odd"
        print(f"Index {index} ({index_type}) -> Value: {value}")

    print("-" * 30)
    print("Sum of elements:", total_sum)
    print("Max value:", max_value)
    print("Index of max value:", max_index)


numbers = [10, 25, 7, 40, 18]
analyze_list(numbers)

def pair_product(numbers, target_product):
  previous_nums = {}

  for index, num in enumerate(numbers):
    complement = target_product / num
    if complement in previous_nums:
      return (previous_nums[complement], index)
      # previous_nums[complement] <- this is taking the value, which is the           index of the value's location in numbers

    previous_nums[num] = index

pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)

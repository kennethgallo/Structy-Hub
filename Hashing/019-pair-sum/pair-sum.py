def pair_sum(numbers, target_sum):
  # for i in range(0, len(numbers)):
  #   for j in range(i+1, len(numbers)):
  #     if numbers[i] + numbers[j] == target_sum:
  #       return (i,j)

  previous_nums = {}

  for index, num in enumerate(numbers):
    compliment = target_sum - num

    if compliment in previous_nums:
      return (previous_nums[compliment], index)

    previous_nums[num] = index
  
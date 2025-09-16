def max_value(nums):
  max = float('-inf')

  for numbers in range(len(nums)):
    if nums[numbers] >= max:
      max = nums[numbers]
  return max
def pair_sum(numbers, target_sum):

  previous = {}

  for index, num in enumerate(numbers):
    complement = target_sum - num
    if complement in previous:
      return(previous[complement], index)
    previous[num] = index


print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)

def sum_of_lengths(strings):
  if len(strings) == 0:
    return 0
    
  return len(strings[0]) + sum_of_lengths(strings[1:])

  # time complexity -> input of n. Copying sub list and running n operations
  # resulting in O(n^2) time

  # space complexity -> input of n. copying each sliced sub list requires n space 
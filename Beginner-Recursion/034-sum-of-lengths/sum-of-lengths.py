def sum_of_lengths(strings):
  if len(strings) == 0:
    return 0
  print(len(strings[0]))
  len(strings[0]) + sum_of_lengths(strings[1:])
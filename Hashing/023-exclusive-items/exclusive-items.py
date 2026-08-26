def exclusive_items(a, b):
  uniques = []

  set_a = set(a)
  set_b = set(b)

  for num in a:
    if num not in set_b:
      uniques.append(num)

  for num in b:
    if num not in set_a:
      uniques.append(num)

  # time complexity -> O(n+m): time to convert lists to sets 
  # and iterate through lists to add to uniques
  # space complexity -> O(n+m): space for creating each set, combined

  return uniques
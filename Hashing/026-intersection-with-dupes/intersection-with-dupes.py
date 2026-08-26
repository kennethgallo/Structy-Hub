def intersection_with_dupes(a, b):
  count_a = {}
  count_b = {}
  dupes = []

  for num in a:
    if num not in count_a:
      count_a[num] = 0
    count_a[num] += 1

  for num in b:
    if num not in count_b:
      count_b[num] = 0
    count_b[num] += 1 

  for key, value in count_a.items():
    if key in count_b:
      for i in range(0, min(value, count_b[key])):
        dupes.append(key)

  # time complexity -> O(n+m): iterating over both lists
  # space complexity -> O(n+m): storing count objects
  
      
  return dupes
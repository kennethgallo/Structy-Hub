def intersection(a, b):
  intersection_list = []
  # for i in a:
  #   for j in b:
  #     if i == j:
  #       intersection_list.append(j)

  b_set = set(b)
  for item in a:
    if item in b_set:
      intersection_list.append(item)
  return intersection_list

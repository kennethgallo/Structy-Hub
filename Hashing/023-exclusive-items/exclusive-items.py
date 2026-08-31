def exclusive_items(a, b):
  set_a = set(a)
  set_b = set(b)

  result = []

  for item in set_a:
    if item not in set_b:
      result.append(item)

  for item in set_b:
    if item not in set_a:
      result
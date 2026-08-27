def exclusive_items(a, b):
  unqiues = []

  set_a = set(a)
  set_b = set(b)

  for ele in set_a:
    if ele not in set_b:
      unqiues.append(ele)

  for num in set_b:
    if num not in set_a:
      unqiues.append(num)

  print(unqiues)
  
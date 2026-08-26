def exclusive_items(a, b):
  exclusives = []
  count = {}

  for num in a:
    if num not in count:
      count[num] = 0
    count[num] += 1

  for num in b:
    if num not in count:
      count[num] = 0
    count[num] += 1 

  for num in count:
    if count[num] == 1:
      exclusives.append(num)

  return exclusives
def exclusive_items(a, b):
  exclusives = []
  count = {}
  # for num in a:
  #   if num not in b:
  #     exclusives.append(num)

  # for ele in b:
  #   if ele not in a:
  #     exclusives.append(ele)

  for num in a:
    if num not in count_a:
      count[num] = 0
    count[num] += 1

  for num in b:
    if num not in count_b:
      count[num] = 0
    count[num] += 1 

  for num in count:
    if count[num] == 1:
      exclusives.append(num)

  #print(count_a, count_b)

  return exclusives
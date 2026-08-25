def intersection(a, b):

  intersection_list = []

  counter = {}

  # for i in a:
  #   if i in b:
  #     intersection_list.append(i)

  for i in a:
    if i not in counter:
      counter[i] = 0
    counter[i] += 1

  for j in b:
    if j in counter:
      intersection_list.append(j)
  intersection_list = []
    
  print(counter)

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]

  #return intersection_list
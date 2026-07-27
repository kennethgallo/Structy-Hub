def most_frequent_char(s):

  count = {}
  most = None

  for char in s:
    if char not in s:
      count[char] = 0
    count[char] += 1

  for i in count:
    if most == None or count[i] > count[most]:
      most = i
  return most
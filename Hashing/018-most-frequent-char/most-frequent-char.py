def most_frequent_char(s):
  count = {}

  most = None

  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1

  for item in count:
    if most == None or count[item] > count[most]:
      most = item

  return most

most_frequent_char('bookeeper') # -> 'e'


  
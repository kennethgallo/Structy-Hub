def most_frequent_char(s):
  most = None
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1

  for item in count:
    if most == None or count[item] > most:
      most = item

  return most
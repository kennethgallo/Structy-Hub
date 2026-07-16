def most_frequent_char(s):

  count = {}
  most = None

  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1

  for letter in count:
    if most == None or count[letter] > count[most]:
      most = letter
  return most

    


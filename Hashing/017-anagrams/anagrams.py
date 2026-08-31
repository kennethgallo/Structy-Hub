def anagrams(s1, s2):
  return count(s1) == count(s2)

def counter(s):

  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  return count
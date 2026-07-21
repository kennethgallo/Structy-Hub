def anagrams(s1, s2):
  return counter(s1) == counter(s2)


def counter(s):
  counter = {}
  
  for char in s:
    if char not in counter:
      counter[char] = 0
    counter[char] += 1
  return counter


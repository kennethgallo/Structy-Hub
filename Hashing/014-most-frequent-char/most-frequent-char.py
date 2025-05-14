from collections import Counter

def most_frequent_char(s):
  count = Counter(s)

  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best
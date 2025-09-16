def longest_word(sentence):
  longest = ""
  words = sentence.split(" ")

  for word in words:
    if len(word) >= len(longest):
      longest = word

  return longest
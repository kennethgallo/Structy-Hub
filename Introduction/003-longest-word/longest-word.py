def longest_word(sentence):
  max_word = ''
  for word in sentence.split(' '):
    if len(word) >= len(max_word):
      max_word = word

  return print(max_word)

#longest_word("what a wonderful world")
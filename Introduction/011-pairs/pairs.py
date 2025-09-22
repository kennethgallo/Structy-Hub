def pairs(elements):
  output = []

  for i in range(0, len(elements)): 
    for j in range(i + 1, len(elements)):
      pair = [elements[i], elements[j]]
      output.append(pair)
    

  return output
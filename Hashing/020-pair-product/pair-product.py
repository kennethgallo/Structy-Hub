def pair_product(numbers, target_product):
  for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] * numbers[j] == target_product:
        return (i,j)
  
  
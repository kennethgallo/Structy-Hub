def fizz_buzz(n):
  solution = []
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      solution.append("fizzbuzz")
    elif i % 3 == 0:
      solution.append("fizz")
    elif i % 5 == 0:
      solution.append("buzz")
    else:
      solution.append(i)

  return solution
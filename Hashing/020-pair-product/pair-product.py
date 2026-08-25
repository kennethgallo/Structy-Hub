def pair_product(numbers, target_product):

  previous_numbers = {}

  for index, num in enumerate(numbers):
    complement = target_product / num

    if complement in previous_numbers:
      return (index, previous_numbers[complement])

    
def all_unique(items):

  unique = set(items)

  for item in items:
    if item not in unique:
      return False
  else:
    return True
def all_unique(items):

  item_set = set()
  
  for item in items:
    if item in item_set:
      return False
    item_set.add(item)
    
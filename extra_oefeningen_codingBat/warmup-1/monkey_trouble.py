def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or ( a_smile == False and b_smile == False):
    return True
  else:
    return False

monkey_trouble(True, False)
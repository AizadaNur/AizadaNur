def near_ten(num):
  if num%10<=2:
    return True
  elif num%10==9 or num%10==8:
    return True
  return False

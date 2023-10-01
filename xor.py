def xor(val):
  if val%4 ==0:
    return val
  elif val%4 == 1:
    return 1
  elif val%4 == 2:
    return 4*(val//4)+3
  return 0

m = 1680
a = 5
b = 16

def is_prime(num):
  if num == 2 or num == 3: return True
  if num < 2 or num%2 == 0: return False
  if num < 9: return True
  if num%3 == 0: return False
  r = int(num ** 0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if num%f == 0: return False
    if num%(f + 2) == 0: return False
    f +=6
  return True
def baseToDec(num, base):
  n = 0
  for i in str(num):
    n = base * n + int(i)
  return n

def decToBase(num, base):
  res = ''
  num = int(num)
  while num:
    res += str(num % base)
    num //= base
  return res[::-1]

def negative(x, y, b):
  if b==10:
    return int(x) - int(y)

  dx=baseToDec(x,b)
  dy=baseToDec(y,b)
  dz=dx-dy
  return decToBase(dz, b)
  
def solution(n, b):
  id_list = []
  while True:
    x = ''.join(sorted(str(n), reverse=True))
    y = ''.join(sorted(str(n)))
    z = negative(x,y,b)
    # There is an issue at this line (base 10), we need to explicitly return int(x) - int(y) when base is 10
    # z = decToBase(baseToDec(x, b) - baseToDec(y, b), b)
    z_len = len(str(z))
    x_len = len(str(x))
    # this will add trailing zero instead of leading zero
    # but this doesn't matter (affect) our result, since i will be k and trailing zero (i is descing digit order)
    # and all we care is the occurrences, this won't affect our result
    if (z_len != x_len):
      z = format(z, '0' + str(x_len))
    '''
    Iterate Stack-like list to check for the current top item of stack equals current
    z. If they equal, there must be a cycle. We can prove that later
    '''
    for i, item in enumerate(id_list):
      if item == z:
        return i + 1
    id_list.insert(0, z)
    n = z

print(solution('1211', 10))
from queue import Queue

q = Queue()
result = ''
str = 'aabcccdddeeff'
strLen = len(str)
str += '\n'
print('Original str:', str)
q.put(str[0])
for index in range(strLen):
  char = str[index]
  nextChar = str[index + 1]
  if char == nextChar:
    q.put(char)
  else:
    size = q.qsize()
    while not q.empty():
      char1 = q.get()
      if size < 3:
        result += char1
    q.put(nextChar)
print('Result:', result[::-1])

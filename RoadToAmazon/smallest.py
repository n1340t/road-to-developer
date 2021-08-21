# https://www.geeksforgeeks.org/build-lowest-number-by-removing-n-digits-from-a-given-number/?fbclid=IwAR3A8sjbBnX4BOUGHi62qy-ufMvMpkX9-KUesIUyJEc621zm2io4hbLfi8k
S = '4615719'
K = 3

sta = [S[0]]

for ch in S[1:]:
  print(sta)
  while sta and K > 0 and sta[-1] > ch and not (len(sta) == 1 and ch =='0'):
    K -= 1
    sta.pop()
  
  sta.append(ch)

sta = sta[:-K or None]
print(''.join(sta))
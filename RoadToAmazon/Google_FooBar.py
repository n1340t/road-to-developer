'''
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big trouble. 

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("abcabcabcabc")
Output:
    4

Input:
solution.solution("abccbaabccba")
Output:
    2
'''
import math

def solution(s):
  # Find all divisor
  i = 1
  divisors = []
  s_length = len(s)
  while i <= math.sqrt(s_length):
    if s_length % i == 0:
      if s_length / i == i:
        divisors.append(i)
      else:
        divisors.append(i)
        divisors.append(s_length / i)
    i += 1
  divisors.sort()
  for divisor in divisors:
    cpm_str = s[:divisor]
    count = s.count(cpm_str)
    if count == s_length / divisor:
      return count

def solution_v2(s):
  s_length = len(s)
  i = 1
  divisors = []
  while i <= math.sqrt(s_length):
    if s_length % i == 0:
      if s_length / i == i:
        divisors.append(i)
      else:
        divisors.append(i)
        divisors.append(s_length / i)
    i += 1
  divisors.sort()
  for divisor in divisors:
    cpm_str = s[:divisor]
    total_parts = s_length / divisor
    for i in range(total_parts):
      if s[i * divisor: (i+1) * divisor] != cpm_str:
        break
      if i == total_parts - 1:
        return total_parts

print(solution_v2('abcde' * 25))
print(solution_v2('abcabcabcabc'))
print(solution_v2('abccbaabccba'))
print(solution_v2('abcabc1abcabcabcabc1abcabc'))
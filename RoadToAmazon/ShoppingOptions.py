'''
Problem statement: An Amazon Customer wants to buy a pair of jeans, a pair of shoes, 
a skirt, and a top but has a limited budget in dollars. Given different pricing options for each product, 
determine how many options our customer has to buy 1 of each product. 
You can not spend more money than the budgeted amount.

priceOfJean = [2,3]
priceOfShoes = [4]
priceOfSkirts = [2,3]
priceofTops = [1,2]

 The customer must buy shoes for 4 dollars since there is only one option. 
 This leaves 6 dollars to spend on the other 3 items. 
 Combination of prices paid for jeans, skirts, and tops respectively that add up to 6 dollars or fewer [2,2,2], [2,2,1], [3,2,1], [2,3,1].
 There are 4 ways the customer can purchase all 4 items.

 Reference:
 https://www.geeksforgeeks.org/amazon-interview-experience-for-software-development-engineer-ii/
 https://leetcode.com/discuss/interview-question/1128534/amazon-oa-2021
 https://leetcode.com/discuss/interview-question/1031663/Amazon-OA
'''

# This simliar to 4 sum II problem
def getNumberOfOptions(priceOfJeans: list, priceOfShoes:list, priceOfSkirts: list, priceOfTops: list, budget: int) -> int:
  jeans_and_shoes = {}
  for jean in priceOfJeans:
    for shoe in priceOfShoes:
      _total = jean + shoe
      if jeans_and_shoes.get(_total):
        continue
      else:
        jeans_and_shoes[_total] = _total

  skirt_and_top = {}
  count = 0
  for skirt in priceOfSkirts:
    for top in priceOfTops:
      _total = budget - skirt - top
      if _total
  print(jeans_and_shoes)
  return 0

priceOfJeans = [2,3]
priceOfShoes = [4]
priceOfSkirts = [2,3]
priceOfTops = [1,2]
budget = 6
getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budget)
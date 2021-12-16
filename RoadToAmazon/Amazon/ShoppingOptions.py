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
 https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-2-4-years-experienced/?ref=rp
 https://leetcode.com/discuss/interview-question/1128534/amazon-oa-2021
 https://leetcode.com/discuss/interview-question/1031663/Amazon-OA
 https://thejoboverflow.com/p/p255/
'''

# This simliar to 4 sum II problem
def getNumberOfOptions(priceOfJeans: list, priceOfShoes:list, priceOfSkirts: list, priceOfTops: list, budget: int) -> int:
  memory1 = [x + y for x in priceOfJeans for y in priceOfShoes]
  memory2 = [x + y for x in priceOfSkirts for y in priceOfTops]
  memory1.sort()
  memory2.sort()
  count = 0
  j = len(memory2) - 1
  for x in memory1:
    while (j >= 0 and x + memory2[j]) > budget:
      j -= 1
    count += j + 1 #plus 1 because j is currently an index, if we want to use j as counter, need plus 1
  
  return count

priceOfJeans = [2,3]
priceOfShoes = [4]
priceOfSkirts = [2,3]
priceOfTops = [1,2]
budget = 12
count = getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budget)
print(count)
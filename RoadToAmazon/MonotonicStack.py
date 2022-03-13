from typing import List
'''
Find next smaller element
Input  [4,5,6,7,2]
Output [4,4,4,4,5]
Explain next element which smaller than 4 is 2
Next element which is smaller than 2 is None or can be think of list length
Approach Monotone Increasing Stack
Property of Monotone Increaseing Stack

When insert
'''

'''
Find next greater element
Approach Monotone Decreasing Stack
'''


class Solution:
    stack = []
    # decreasing stack - Ex: [4,3,2,1]

    def next_greater_elem(self, nums: List[int]) -> None:
        print('Iteration starts at the beginning (Left to right)')
        # use stack to store index => track by index
        N = len(nums)
        next_greater = [-1] * N
        for i in range(N):
            # replicate monotonic stack push operation
            while self.stack and nums[self.stack[-1]] < nums[i]:
                next_greater[self.stack[-1]] = nums[i]
                self.stack.pop()
            self.stack.append(i)
        print(nums)
        print(next_greater)

    def next_greater_elem_iterate_start(self, nums: List[int]) -> None:
        print('Iteration starts at the end (Right to Left')
        self.stack = []
        next_greater = [-1] * len(nums)
        # iterate backward method
        for i in range(len(nums) - 1, -1, -1):
            while self.stack and nums[i] > nums[self.stack[-1]]:
                self.stack.pop()
            next_greater[i] = nums[self.stack[-1]] if self.stack else -1
            self.stack.append(i)
        print(nums)
        print(next_greater)


if __name__ == '__main__':
    sol = Solution()
    nums = [13, 7, 6, 12]
    sol.next_greater_elem_iterate_start(nums)

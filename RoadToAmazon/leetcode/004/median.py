class Solution:
    # Time is O(n), Space is O(1)
    def getMedianSameSize1(self, arr1, arr2, n):
        # median of each array
        m1 = m2 = -1
        i = j = count = 0
        while count <= n:
            count += 1
            if arr1[n - 1] <= arr2[0]:
                m1 = arr1[n - 1]
                m2 = arr2[0]
                break
            elif arr1[0] >= arr2[n - 1]:
                m1 = arr1[0]
                m2 = arr2[n - 1]
                break

            if arr1[i] <= arr2[j]:
                m1 = m2
                m2 = arr1[i]
                i += 1
            else:
                m1 = m2
                m2 = arr2[j]
                j += 1
        return (m1 + m2) / 2
    def getMedianSameSize2(self, arr1, arr2):
        return len(arr1)

if __name__ == '__main__':
    sol = Solution()
    print('Median of two arrays with same size')
    print('Test case #1: at least one element of arr1 is greater than any element of arr2')
    num1 = [1, 12, 15, 26, 38]
    num2 = [2, 13, 17, 30, 45]
    median = sol.getMedianSameSize1(num1, num2, len(num1))
    print('median', median)
    print('Test case #2: No element of arr1 is greater than any element of arr2')
    num1 = [1, 12, 15, 26, 38]
    num2 = [42, 43, 47, 330, 560]
    median = sol.getMedianSameSize2(num1, num2, len(num1))
    print('median', median)
    print('Test case #3: array with size of 1')
    num1 = [4]
    num2 = [5]
    median = sol.getMedianSameSize3(num1, num2, len(num1))
    print('median', median)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        leftSum = 1
        rightSum = 1
        left = [1]
        right = [1]
        
        for i in range(length):
            first = i
            last = length - i - 1

            if first != length - 1:
                leftSum *= nums[first]
                left.append(leftSum)

            if last != 0:
                rightSum *= nums[last]
                right.append(rightSum)

        for i in range(length):
            first = i
            last = length - i - 1
            product = left[first] * right[last]
            nums[i] = product

        return nums
            

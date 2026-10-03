class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        if(len(nums) == 2): 
            return [0, 1]

        for i in range(len(nums)):
            current = target - nums[i]
            if(current in count):
                return [count[current], i]
            count[nums[i]] = i

        
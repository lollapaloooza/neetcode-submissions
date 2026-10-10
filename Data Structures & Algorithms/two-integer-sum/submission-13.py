class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        if(len(nums) == 2):
            return [0, 1]

        for i in range(len(nums)):
            curr = target - nums[i]

            if(curr in count):
                return [count[curr], i]

            count[nums[i]] = i
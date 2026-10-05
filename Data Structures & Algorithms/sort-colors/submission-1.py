class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            if(count[0] > 0):
                nums[i] = 0
                count[0] -= 1
                continue
            
            if(count[1] > 0):
                nums[i] = 1
                count[1] -= 1
                continue

            if(count[2] > 0):
                nums[i] = 2

        
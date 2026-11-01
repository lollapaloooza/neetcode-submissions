class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        curr = 0
        for color in range(3):
            for i in range(count[color]):
                nums[curr] = color
                curr += 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        one, two = 0, len(nums) - 1

        while(one <= two):
            if(nums[one] == val):
                nums[one] = nums[two]
                two -= 1
            else:
                one += 1

        return one
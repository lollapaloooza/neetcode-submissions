class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sint(idx, maxLength):
            while(2*idx + 1 < maxLength):
                leftChild, rightChild = 2*idx + 1, 2*idx + 2
                biggestChild = leftChild

                if(rightChild < maxLength):
                    biggestChild = leftChild if nums[leftChild] > nums[rightChild] else rightChild
                
                if(nums[biggestChild] > nums[idx]):
                    nums[idx], nums[biggestChild] = nums[biggestChild], nums[idx]
                    idx = biggestChild
                else:
                    break
        
        lastParent = len(nums) // 2 - 1

        for i in range(lastParent, -1, -1):
            sint(i, len(nums))

        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            sint(0, i)

        return nums
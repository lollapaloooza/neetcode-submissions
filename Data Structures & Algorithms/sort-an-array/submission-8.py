class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def bro(i, maxLength):
            idx = i

            while(idx*2 + 1 < maxLength):
                leftChild = idx * 2 + 1
                rightChild = idx * 2 + 2

                biggestChild = leftChild

                if(rightChild < maxLength):
                    biggestChild = leftChild if nums[leftChild] >= nums[rightChild] else rightChild
                
                if(nums[biggestChild] > nums[idx]):
                    nums[biggestChild], nums[idx] = nums[idx], nums[biggestChild]
                    idx = biggestChild
                else:
                    break

                
        minParent = len(nums) // 2 - 1
        
        for i in range(minParent, -1, -1):
            bro(i, len(nums))
        
        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            bro(0, i)

        return nums

        



10,9,1,1,1,2,3,1

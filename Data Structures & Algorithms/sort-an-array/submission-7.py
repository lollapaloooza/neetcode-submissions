class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sint(idx, maxLength):
            i = idx
            while 2*i + 1 < maxLength:
                leftChild, rightChild = 2*i + 1, 2*i + 2
                biggestChild = leftChild

                # print(idx, leftChild, rightChild, maxLength, 'inside')
                # print(nums[idx], nums[leftChild], 'index leftChild')
                if rightChild < maxLength:
                    # print(nums[rightChild], 'rightChild')
                    biggestChild = leftChild if nums[leftChild] >= nums[rightChild] else rightChild
                
                if nums[biggestChild] > nums[i]:
                    nums[i], nums[biggestChild] = nums[biggestChild], nums[i]
                    i = biggestChild
                else:
                    break
                

            
        parent = len(nums) // 2 - 1

        for index in range(parent, -1, -1):
            sint(index, len(nums))
        
        # print(nums, 'before sint and swap')
        for index in range(len(nums) - 1, -1, -1):
            nums[0], nums[index] = nums[index], nums[0]
            # print(nums, 'after swap')
            sint(0, index)
            # print(nums, 'after sint')

        return nums


        


        
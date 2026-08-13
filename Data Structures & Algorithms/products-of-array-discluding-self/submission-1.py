class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # You are multiplying every number inside the list except the number it self. So for each num, you multiply the num by its neighbors but you don't multiply the num itself.
        # Ex: list = [1,2,4,6] say you're for looping and start at 1. You're multiplying 2 * 4 * 6. Notice you're not multiplying 1. Next iteration,  you're at 2. 4 * 6 * 1. You're not multiplying 2. You contiune doing this until you finish and have all the nums covered
        output = [1] * len(nums)
        right = 1
        left = 1
        for j in range(len(nums)-1,-1,-1):
            output[j] = right
            right *= nums[j]
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        return output

        

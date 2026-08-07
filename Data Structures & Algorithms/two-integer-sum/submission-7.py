class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap.keys():
                return [hashmap[complement],i]
            hashmap[num] = i


        """
        Whenever i have to match a number to its indices, count or
        vise versa, expect an hashmap

        I can make a hashmap and set the key to the int and value to the index.
        How do i find which two values in the hashmap = target without O(n^2)?
        """
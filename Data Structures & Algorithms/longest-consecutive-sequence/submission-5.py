class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        We are given a list of nums and must check for its consectutive freqency(CF), then I return the length of that frequency. Consecutive frequency meaning, each num is supposed to be exactly 1 greater than the num before it.
        I.E: [2,3,4,5] then we need the length of this sequence which in this case is 4.

        So what can we do given what we know? This is nothing realted to frequency, I can't find out from the current list, but I can make a seperate list that contains all the nums in CF. 
        I want to transverse through the list, but can I find the info needed with that list tho? Also, How can I check if a number is exactly one bigger then it whats before it. 
        
        I need to start with the smallest number. Then I want to build a list of CF's and just return that list... Just how? How can I check if a number is exactly 1 more then the prev num.
        """
        cf = 0
        longest = 0
        hashmap = {}
        current = 1
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for num in hashmap:
            if num - 1 not in hashmap:
                current = num
                cf = 0
                cf += 1
                while current in hashmap:
                    if current + 1 not in hashmap:
                        if longest < cf:
                            longest = cf    
                        break        
                    current = current + 1
                    cf += 1
        return longest      
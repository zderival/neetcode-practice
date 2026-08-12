class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # You're looking at a  integer list (nums), and finding elements in the list that consdiered the most freqent. int k is what are the most k frequent elements in the aray. What do we define as frequent? What elements are the most shown based off count. You're returning k elements with the highest count.
        hashmap = {}
        frequent_nums = []
        for i, num in enumerate(nums):
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                 hashmap[num] = 1

        while len(frequent_nums) != k:
            max_num = 0
            max_num_freq = 0
            for num in hashmap:
                if max_num_freq < hashmap[num]:
                    max_num_freq = hashmap[num]
                    max_num = num
            frequent_nums.append(max_num)
            hashmap.pop(max_num)            
        return frequent_nums
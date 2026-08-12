class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # You're looking at a  integer list (nums), and finding elements in the list that consdiered the most freqent. int k is what are the most k frequent elements in the aray. What do we define as frequent? What elements are the most shown based off count. You're returning k elements with the highest count.
        hashmap = {}
        frequent_nums = []
        buckets = [[] for _ in range(len(nums) + 1)]
        for index, num in enumerate(nums):
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                 hashmap[num] = 1
        for num in hashmap:
            frequency = hashmap[num]
            buckets[frequency].append(num)
        for i in range(len(buckets)-1,-1,-1):
            if len(frequent_nums) == k:
                break
            else:
                frequent_nums.extend(buckets[i][:k - len(frequent_nums)])

        return frequent_nums

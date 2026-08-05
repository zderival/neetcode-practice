class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] = s_dict[char] + 1
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] = t_dict[char] + 1
            
        if s_dict == t_dict:
            return True
        else:
            return False

    # s and t are two full strings
    # function requires an boolean to return
    # two strings must anagrams of each other
    # Anagram - a string that has the same characters in another string...not the same length
    # Notice in case 2 that they are the same length but not the same chars
# You just need to know the contents inside each string, not the length


class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = ""
        s = s.lower()

        for l in range(len(s)):
            if(not s[l].isalnum()):
                continue
            else:
                check_string = check_string + s[l]
        if(not check_string):
            return True
            
        i = 0
        j = len(check_string) - 1

        while(check_string[i] == check_string[j]):
                i = i + 1
                j = j - 1
                if(i > j):
                    return True
        return False
        
        # lower = s.lower().strip()
        # j = len(lower) - 1
        # for i in range(len(lower)):
        #     if lower[i] == lower[j]:
        #         j--
        #         continue
        #     else:
        #         print(lower[i])
        #         print(lower[j])
        #         return False
        # return True
class Solution:

    def encode(self, strs: List[str]) -> str:
        # You need a set of rules that gives a characteristc for each string to follow in order to definitivly tell between which string is what. Then include those characteristics in a string.
        # What can I say for each string in the list given to me, that'll make them different from each other?
        encoded = ""
        for string in strs:
            string_info = f"{len(string)}#{string}"
            encoded += string_info
        return encoded.strip()
    def decode(self, s: str) -> List[str]:
        # I want to remove the first len(string)# then select the entrie string up to len(string)# and set that portion of the string into a list, keep doing this on a loop till s == ""
        decoded = []
        position = 0
        while position < len(s):
            i = s.index("#",position)
            length = int(s[position:i])
            word = s[i+1 : i+1+length]
            decoded.append(word)
            position = i + 1 + length
        return decoded



            
                    

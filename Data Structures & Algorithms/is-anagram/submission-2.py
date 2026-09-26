class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): 
            return False

        count = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - 97
            idx2 = ord(t[i]) - 97
            count[idx] += 1
            count[idx2] -= 1

        return not any(count)
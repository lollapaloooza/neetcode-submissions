class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        idx = 0

        for i in range(len(first)):
            for word in strs:
                if(len(word) - 1 < i or word[i] != first[i]):
                    return first[:idx]
            idx += 1

        return first[:idx]
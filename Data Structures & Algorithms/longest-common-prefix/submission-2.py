class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        if(len(strs) == 1):
            return common

        for i in range(len(strs) - 1):
            word = strs[i + 1]
            
            curr = common

            while(not word.startswith(curr)):
                curr = curr[:-1]

            common = curr
            
            if(not curr):
                return ""
        
        return common

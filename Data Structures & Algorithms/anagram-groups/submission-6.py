class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count)

            anagrams[key].append(word)

        return list(anagrams.values())

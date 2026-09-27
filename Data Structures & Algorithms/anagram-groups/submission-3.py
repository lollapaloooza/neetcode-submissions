class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            sort = sorted(anagram)
            key = tuple(sort)

            anagrams[key].append(anagram)

        return list(anagrams.values())
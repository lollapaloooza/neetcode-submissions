class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            anagrams[tuple(sorted(anagram))].append(anagram)

        return list(anagrams.values())



        # anagrams = defaultdict(list)

        # for anagram in strs:
        #     key = [0] * 26

        #     for letter in anagram:
        #         idx = ord(letter) - ord("a")
        #         key[idx] += 1


        #     strKey = tuple(key)
        #     anagrams[strKey].append(anagram)

        # return list(anagrams.values())
class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0

        while(idx < len(s)):
            pound = s.find("#", idx)
            length = int(s[idx:pound])

            start = pound + 1
            end = start + length

            word = s[start:end]
            strs.append(word)

            idx = end

        return strs

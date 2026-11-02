class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}|{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0

        while idx < len(s):
            start = s.find("|", idx)
            number = int(s[idx:start])
            end = number + start + 1

            strs.append(s[start + 1:end])

            idx = end

        return strs
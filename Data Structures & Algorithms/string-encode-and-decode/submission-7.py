class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append('sample')
        print(strs)
        return "|_".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s, s.split("|_"))
        strs = s.split("|_")
        return strs[:-1]
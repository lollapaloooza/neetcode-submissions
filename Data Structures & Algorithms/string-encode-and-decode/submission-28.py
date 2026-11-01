class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append('sample')
        return "|_".join(strs)

    def decode(self, s: str) -> List[str]:
        strs = s.split("|_")
        return strs[:-1]
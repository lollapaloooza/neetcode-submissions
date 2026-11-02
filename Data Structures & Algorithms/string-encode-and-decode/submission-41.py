class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word)}|{word}"

        return string

    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        idx = 0
        while(idx < len(s)):
            numberPointer = idx

            while(s[numberPointer] != "|"):
                numberPointer += 1

            number = int(s[idx:numberPointer])

            idx = numberPointer + 1
            strs.append(s[idx: idx + number])

            idx += number

        return strs
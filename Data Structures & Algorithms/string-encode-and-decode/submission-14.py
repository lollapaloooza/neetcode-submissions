class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word)}#{word}"

        return string


    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        number = ""

        while(idx < len(s)):
            if(s[idx] == "#"):
                word = ""
                j = 0

                if(int(number) != 0):
                    idx += 1
                else:
                    number = 0
                    idx += 1


                while(j < int(number)):
                    word += s[idx]
                    idx += 1
                    j += 1

                strs.append(word)
                number = ""
            else:
                number += s[idx]
                idx += 1

        return strs


            
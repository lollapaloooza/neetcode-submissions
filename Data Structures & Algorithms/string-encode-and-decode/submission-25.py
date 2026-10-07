class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word)}#{word}"

        return string


    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        number = []

        while(idx < len(s)):
            if(s[idx] == "#"):
                j = 0
                length = "".join(number)

                if(length == ""):
                    length = 0

                idx += 1

                word = s[idx:idx+int(length)]
                
                idx += int(length)

                strs.append(word)
                
                number.clear()
            else:
                number.append(s[idx])
                idx += 1

        return strs


            
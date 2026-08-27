class Solution:

    # def encode(self, strs: list[str]) -> str:
    #     x = []
    #     for s in strs:
    #         header = str(len(s)).zfill(4)
    #         x.append(header+s)
    #     return "".join(x)

        
    # def decode(self, s: str) -> list[str]:
    #     y = []
    #     i = 0
    #     while i < len(s):
    #         l = s[i:i+4]
    #         n = int(l)
    #         b = s[i+4:i+4+n]
    #         y.append(b)
    #         i = i+4+n
    #     return y


    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s):04d}{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        y, i = [], 0
        while i < len(s):
            n = int(s[i : i + 4])
            y.append(s[i + 4 : i + 4 + n])
            i += 4 + n
        return y
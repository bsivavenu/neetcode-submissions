class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r, i, j = 0, len(word), 0, len(abbr)

        while l < r and i < j:
            if abbr[i] == "0":
                return False

            if word[l] == abbr[i]:
                i += 1
                l += 1
            elif abbr[i].isalpha():
                return False
            else:
                sum = 0
                while i < j and abbr[i].isdigit():
                    sum = sum * 10 + int(abbr[i])
                    i += 1
                l = l + sum
        return l == r and i ==j
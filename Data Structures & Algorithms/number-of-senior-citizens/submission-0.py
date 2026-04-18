class Solution:
    def countSeniors(self, details: List[str]) -> int:
        x = [i for i  in details if int(i[11:13])>60 ]
        return len(x)
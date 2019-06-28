class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res,res2 = [],[]
        for x in A:
            if x % 2 == 0:
                res.append(x)
            else:
                res2.append(x)
        return res+res2
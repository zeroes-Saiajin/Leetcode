class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = []
        even = [x for x in A if x % 2 == 0]
        odd = [y for y in A if y % 2 != 0]
        for x, y in zip(even, odd):
            res.append(x)
            res.append(y)

        return res
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[abs(y-1) for y in x][::-1] for x in A]
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for nums in A:
            if A.count(nums) > 1:
                return nums
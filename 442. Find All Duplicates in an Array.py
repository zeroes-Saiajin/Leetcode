from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [i for i in count if count[i] == 2 ]

#class Solution:
#    def findDuplicates(self, nums: List[int]) -> List[int]:
#        res, count = [], set()
#        for i in nums:
#            if i not in count:
#                count.add(i)
#            else:
#                res.append(i)
#        return res
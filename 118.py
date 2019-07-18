class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1 for i in range(j+1)]for j in range(numRows)]
        for x in range(2, numRows):
            for y in range(1, x):
                nums[x][y] = nums[x-1][y-1] + nums[x-1][y]
        return nums
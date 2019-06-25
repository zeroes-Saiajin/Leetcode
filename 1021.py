class Solution:
    def __init__(self):
        self.stack = []
        self.result = ''
        self.right = ''
    def removeOuterParentheses(self, S: str) -> str:
        for i in S:
            if i == '(':
                self.stack.append(i)
            else:
                self.stack.pop()
            self.right += i

            if not self.stack:
                self.result += self.right[1:-1]
                self.right = ''
        return self.result
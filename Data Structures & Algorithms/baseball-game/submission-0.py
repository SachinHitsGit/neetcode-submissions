class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i in "+CD":
                if i == "+":
                    a = stack[-1]
                    b = stack[-2]
                    stack.append(a + b)
                elif i == "C":
                    stack.pop()
                elif i == "D":
                    a = stack[-1]
                    stack.append(a*2)
            else:
                stack.append(int(i))
        s = 0
        print(stack)
        for i in stack:
            s += i
        return s
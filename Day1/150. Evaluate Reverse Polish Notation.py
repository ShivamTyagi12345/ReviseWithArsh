class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        l = len(tokens)
        for i in range(l):
            item =  tokens[i]
            size = len(stack)
            if item in ["+","-","*","/"] and size >=2 :
                a, b = stack.pop(), stack.pop()
                # print("true", a, b)
                if item == "+":
                    stack.append(a+b)
                    # print(stack)
                elif item == "-":
                    stack.append(b-a)
                    # print(stack)
                elif item == "/":
                    stack.append(int(b/a))
                    # print(stack)
                elif item == "*":
                    stack.append(a*b)
                    # print(stack)
            else:
                stack.append(int(item))
        # print(stack)
        if len(stack) == 1:
            return stack[0]
        return -1
                

                
        
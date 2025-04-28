# Problem 20




def isValid(s):
    list1 = list(s)
    stack = []
    for char in list1:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' and len(stack) != 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']' and len(stack) != 0:
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}' and len(stack) != 0:
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False
        
        
print(isValid(']'))

            
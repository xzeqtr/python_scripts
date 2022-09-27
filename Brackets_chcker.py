def checker(s):
    opening_brackets = '([{'
    closing_brackets = ')]}'
    stack = []
    for c in s:
        if c in closing_brackets:
            if not stack:
                return False
            else:
                if opening_brackets.index(stack.pop()) != closing_brackets.index(c):
                    return False
        elif c in opening_brackets:
            stack.append(c)
    return not stack
            
                
print(checker('({[balanced]([brackets])})'))
print(checker('{unbalanced()brackets}]'))
print(checker('empty string'))

expression = "{[{iHTSc}]}p(R)m(){q({})"

def keepParenthesis(chaine: str):
    chars = "[]{}()"
    return ''.join([char for char in chaine if char in chars])


def goodExpression(expression: str):

    correspondances = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    stack = []

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) > 0:
                if stack.pop() != correspondances[char]:
                    return False
            else:
                return False
        
    return len(stack) == 0


if goodExpression(keepParenthesis(expression)):
    print("true")
else:
    print("false")
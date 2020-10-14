"""main.py

Name: Tanner Shimanek
Class: CS 2810
Date: October 10, 2020
"""

from stack import Stack


output = ''


def isOperator(char):
    """Check if parameter is an operator."""
    OPERATORS = '+-*/'
    return char in OPERATORS


def getPrecedence(c):
    """Return the precedence of the paramater."""
    result = 0
    OPERATORS = '+-*/'
    for char in OPERATORS:
        result += 1
        if char == c:
            if c in '-/':
                result -= 1
            break
    return result


def expr_is_string(expr):
    """Return True if expression is string type, if not raise ValueError."""
    try:
        if type(expr) is str:
            return True
        else:
            raise ValueError('Expression is not a string.')
    except ValueError as err:
        print(err)
        raise


def valid_infix(expr):
    """Return True if the expression is a valid infix, if not raise SyntaxError."""
    left_bracket = 0
    right_bracket = 0
    for char in expr.replace(" ", ""):
        if char == '(':
            left_bracket += 1
        elif char == ')':
            right_bracket += 1
    try:
        if left_bracket == right_bracket:
            return True
        else:
            raise SyntaxError('Invalid infix expression.')
    except SyntaxError as err:
        print(err)
        raise


def valid_postfix(expr):
    """Returns True if a valid postfix, raises SyntaxError if not valid."""
    expr_list =  [char for char in expr]
    length_of_list = len(expr_list)
    try:
        if length_of_list > 1:
            try:
                if not isOperator(expr_list[0]) and not isOperator(expr_list[1]):
                    elem_1 = expr_list[0]
                    elem_2 = expr_list[1]
                else:
                    raise SyntaxError('Not a valid postfix expression.')
            except SyntaxError as err:
                print(err)
                raise
            try:
                if isOperator(expr_list[-1]):
                    return True
                else:
                    raise SyntaxError('Not a valid postfix expression.')
            except SyntaxError as err:
                print(err)
                raise
        elif length_of_list == 1:
            try:
                if not isOperator(expr_list[0]):
                    return True
                else:
                    raise SyntaxError('Not a valid postfix expression.')
            except SyntaxError as err:
                print(err)
                raise
        elif length_of_list < 1:
            raise SyntaxError('Not a valid postfix expression.')
    except SyntaxError as err:
        print(err)
        raise


def in2post(expr):
    """Convert infix expression to postfix expression."""
    global output
    infix = ''
    postfix = ''
    stack = Stack()
    valid_param = False

    if expr_is_string(expr):
        valid_param = True
        if valid_infix(expr):
            valid_param = True
        else:
            valid_param = False
    else:
        valid_param = False

    if valid_param is True:
        for char in expr.replace(" ", ""):
            infix += char
            if char in '0123456789':
                postfix += char
            elif isOperator(char):
                while True:
                    if stack.size() != 0:
                        topChar = stack.top()
                    else:
                        topChar = None

                    if stack.isEmpty() or topChar == '(':
                        stack.push(char)
                        break
                    else:
                        charPrecedence = getPrecedence(char)
                        topCharPrecedence = getPrecedence(topChar)
                        if charPrecedence > topCharPrecedence:
                            stack.push(char)
                            break
                        else:
                            postfix += stack.pop()
            elif char == '(':
                stack.push(char)
            elif char == ')':
                pop = stack.pop()
                while pop != '(':
                    postfix += pop
                    pop = stack.pop()

        while not stack.isEmpty():
            pop = stack.pop()
            postfix += pop

        output += f'infix: {infix}\n'
        output += f'postfix: {postfix} \n'
    return postfix


def eval_postfix(expr):
    """Evaluates the postfix parameter and returns the solution."""
    global output
    valid_param = False
    stack = Stack()

    if expr_is_string(expr):
        valid_param = True
        if valid_postfix(expr):
            valid_param = True
        else:
            valid_param = False
    else:
        valid_param = False

    if valid_param is True:
        for char in expr.replace(" ", ""):
            if char in '0123456789':
                stack.push(char)
            elif isOperator(char):
                right = stack.pop()
                left = stack.pop()
                if char == '*':
                    ans = lambda left, right: (float(left) * float(right))
                    stack.push(ans(left, right))
                elif char == '/':
                    ans = lambda left, right: (float(left) / float(right))
                    stack.push(ans(left, right))
                elif char == '+':
                    ans = lambda left, right: (float(left) + float(right))
                    stack.push(ans(left, right))
                elif char == '-':
                    ans = lambda left, right: (float(left) - float(right))
                    stack.push(ans(left, right))
    answer = stack.pop()
    output += f'answer: {answer}\n\n'
    return answer


def main():
    file = open('data.txt', 'r')
    lines = file.readlines()
    for line in lines:
        eval_postfix(in2post(line.replace('\n', '')))
    print(output)


main()


def stack_testing():
    """Use this function for testing the stack and main functions.

    - Test eval_postfix() for invalid postfix.
    - Test eval_postfix() for non-string parameters.

    - Test in2post() for invalid infix expressions.
    - Test in2post() for non string parameters.

    - Test Stack() for empty scenarios.
    - Test Stack() for clearing the stack.
    NOTE: REMEMBER TO COMMENT OUT main() while testing.
    NOTE: REMOVE BEFORE SUBMISSION.
    """
    stack = Stack()
    # infix_pass = '8*(5+3)'
    # infix_fail_1 = '8*(5+3))'
    # infix_fail_2 = 8*8
    postfix_pass = '853+*'
    # postfix_fail_1 = '8*5'
    postfix_fail_2 = 8*5

    # print(valid_infix(infix_fail_1))
    # print(eval_postfix(postfix_fail_2))
    print(valid_postfix(postfix_pass))

    # stack.push(5)
    # stack.push(10)
    # l = stack.pop()
    # r = stack.pop()
    # print(l * r)

    # pf = '79*7+56*-3+4-'
    # eval_postfix(pf)



# stack_testing()

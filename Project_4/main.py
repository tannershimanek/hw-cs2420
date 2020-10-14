"""main.py

Name: Tanner Shimanek
Class: CS 2810
Date: October 10, 2020
"""

from stack import Stack


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


def in2post(expr):
    """Convert infix expression to postfix expression."""
    infix = ''
    postfix = ''
    stack = Stack()
    valid_param = False

    # Check for valid parameters
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

        print(f'infix: {infix}')
        print(f'postfix: {postfix} \n')
    return postfix


def eval_postfix(expr):
    # TODO if invalid postfix.. raise a SyntaxError
    # TODO if a non-string.. raise ValueError
    # return result
    pass


def main():
    # TODO CLEAN UP
    print('\n\n **************************** \n\n')


    file = open('data.txt', 'r')
    lines = file.readlines()
    for line in lines:
        in2post(line.replace('\n', ''))



    print('\n\n **************************** \n\n')


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
    infix_pass = '8*(5+3)'
    infix_fail_1 = '8*(5+3))'
    infix_fail_2 = 8*8
    postfix_pass = '853+*'
    postfix_fail_1 = '8*5'
    postfix_fail_2 = 8*5

    # expr_is_string(10)
    # print(valid_infix(infix_fail_1))



stack_testing()

""" TODO """
# 1. open file data.txt.
# 2. read infix expression from the file.
# 3. display the infix expression.
# 4. call function in2post(expr) which takes an infix expression as an
#    input and returns an equivalent postfix expression as a string. 
#    Raise ValueError if the parameter expr is not a string.
# 5. display the postfix expression.
# 6. call function eval_postfix(expr) whihc take a postfix string as an
#    input and returns a number. Raise SyntaxError if the expression is not valid.
# 7. display the result of eval_postfix()



""" postfix expression """
# https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
# https://stackoverflow.com/questions/42703422/infix-to-postfix-algorithm-in-python

""" evaluation postfix """
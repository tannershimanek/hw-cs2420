"""main.py

Name: Tanner Shimanek
Class: CS 2810
Date: October 10, 2020
"""

from stack import Stack

OUTPUT = '\n'


def is_operator(char):
    """Check if parameter is an operator."""
    OPERATORS = '+-*/'
    return char in OPERATORS


def get_precedence(c):
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
    parse = expr.replace(" ", "")
    expr_list =  [char for char in parse]
    length_of_list = len(expr_list)
    try:
        if length_of_list > 1:
            try:
                if not is_operator(expr_list[0]) and not is_operator(expr_list[1]):
                    elem_1 = expr_list[0]
                    elem_2 = expr_list[1]
                else:
                    raise SyntaxError('Not a valid postfix expression.')
            except SyntaxError as err:
                print(err)
                raise
            try:
                op_count = 0
                num_count = 0
                for item in expr_list:
                    if is_operator(item):
                        op_count += 1
                    else:
                        num_count +=1
                if num_count - 1 == op_count:
                    num_count = 0
                    op_count = 0
                else:
                    raise SyntaxError('Not a valid postfix expression.')
            except SyntaxError as err:
                print(err)
                raise
            try:
                if is_operator(expr_list[-1]):
                    return True
                else:
                    raise SyntaxError('Not a valid postfix expression.')
            except SyntaxError as err:
                print(err)
                raise

        elif length_of_list == 1:
            try:
                if not is_operator(expr_list[0]):
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
    global OUTPUT
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
            if char in '0123456789':
                postfix += char
            elif is_operator(char):
                while True:
                    if stack.size() != 0:
                        top_char = stack.top()
                    else:
                        top_char = None

                    if stack.is_empty() or top_char == '(':
                        stack.push(char)
                        break
                    else:
                        char_precedence = get_precedence(char)
                        top_char_precedence = get_precedence(top_char)
                        if char_precedence > top_char_precedence:
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

        while not stack.is_empty():
            pop = stack.pop()
            postfix += pop

        OUTPUT += f'infix: {expr}\n'
        OUTPUT += f'postfix: {postfix}\n'
    return postfix


def eval_postfix(expr):
    """Evaluates the postfix parameter and returns the solution."""
    global OUTPUT
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
            elif is_operator(char):
                right = stack.pop()
                left = stack.pop()
                if char == '*':
                    ans = float(left) * float(right)
                    stack.push(ans)
                elif char == '/':
                    ans = float(left) / float(right)
                    stack.push(ans)
                elif char == '+':
                    ans = float(left) + float(right)
                    stack.push(ans)
                elif char == '-':
                    ans = float(left) - float(right)
                    stack.push(ans)
    answer = stack.pop()
    OUTPUT += f'answer: {float(answer)}\n\n'
    return float(answer)


def main():
    """Opens the file and reads lines, feeding data
       into in2post() and eval_postfix()."""
    file = open('data.txt', 'r')
    lines = file.readlines()
    for line in lines:
        eval_postfix(in2post(line.replace("\n", "")))
    print(OUTPUT[:-1])

main()

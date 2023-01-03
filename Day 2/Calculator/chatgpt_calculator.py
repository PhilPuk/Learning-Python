def calculate(expression):
    # split the expression into tokens
    tokens = expression.split(" ")
    
    # create a stack to hold the values
    values = []
    
    # iterate over the tokens
    for token in tokens:
        try:
            # if the token is a number, convert it to a float and push it onto the stack
            values.append(float(token))
        except ValueError:
            # if the token is an operator, pop the top two values from the stack, apply the operator, and push the result back onto the stack
            if token == "+":
                values[-2] += values[-1]
            elif token == "-":
                values[-2] -= values[-1]
            elif token == "*":
                values[-2] *= values[-1]
            elif token == "/":
                values[-2] /= values[-1]
            elif token == "^":
                values[-2] = values[-2] ** values[-1]
            else:
                # if the token is not a recognized operator, raise an exception
                raise ValueError("Invalid operator: " + token)
            values.pop()
    
    # if there is more than one value left in the stack, raise an exception
    if len(values) != 1:
        raise ValueError("Invalid expression: " + expression)
    
    # return the result
    return values[0]

# test the calculator
print(calculate("2 3 +"))  # prints 5.0
print(calculate("2 3 * 5 +"))  # prints 11.0
print(calculate("2 3 /"))  # prints 0.6666666666666666
print(calculate("2 3 ^"))  # prints 8.0
values = [] # empty list

def getUserValues():
    while True:
        #User Inputs values
        value = input("Enter a number or 'done' to finish: ")
        
        if value == "done":
            break
        #Convert to integer
        value = int(value)
        values.append(value)

def getOperators():
    return str(input("Enter all operators: "))

def calculate(operators):
    result = values[0]  # start with the first value
    
    # iterate over the operators and values
    for i in range(len(operators)):
        operator = operators[i]
        value = values[i + 1]  # get the next value
        
        if operator == "+":
            result += value
        elif operator == "-":
            result -= value
        elif operator == "*":
            result *= value
        elif operator == "/":
            result /= value
    
    return result


def calculatorMain():
    getUserValues()
    print(values)
    operators = getOperators()
    print(operators)
    result = calculate(operators)
    print(result)

#Main Programm
calculatorMain()
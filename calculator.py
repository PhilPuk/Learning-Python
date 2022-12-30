def add(x, y):
    return x + y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

#Main programm
x = float(input('Enter value x: '))
y = float(input('Enter value y: '))
choice = input('(1) Add (2) Substract (3) Multiply (4) Divide Input:')

if choice == 1:
    result = add(x,y)
elif choice == 2:
    result = substract(x,y)
elif choice == 3:
    result = multiply(x,y)
elif choice == 4:
    result = divide(x,y)
else:
    print('Invalid operation!')

print(result)




def add(x, y):
    return x + y

def substract(x,y):
    return x - y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y

#Main programm
val_x = float(input('Enter value x: '))
val_y = float(input('Enter value y: '))
user_choice = int(input('(1) Add (2) Substract (3) Divide (4) Multiply Enter: '))

if user_choice == 1:
    result = add(val_x, val_y)
elif user_choice == 2:
    result = substract(val_x, val_y)
elif user_choice == 3:
    result = divide(val_x, val_y)
elif user_choice == 4:
    result = multiply(val_x, val_y)
else:
    print('Wrong input!')

print(result)
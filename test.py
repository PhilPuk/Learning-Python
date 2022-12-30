print("Hello world!")

x = 10

print(x)

letters = "Amecke"

print("Spell the Letters:")

for i in letters:
    print(i)

print("Count from 0 to 9: ")

for i in range(10):
    print(i)

print("Count from 5 to 0: ")
count = 5
while count >= 0:
    print(count)
    count-= 1

print("Output the values of the array")
prices = [1,2,7,3,9]

prices.append(91)

for i in prices:
    print(i)
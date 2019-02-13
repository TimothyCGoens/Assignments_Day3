print("Hello and welcome to the Factorial Factory!")
print("""Prepare to be amazed as we take any number you give us and give to you,
it's Fantastic Factorial""")

factor = int(input("Please enter any number you wish: "))

def factorial(num):
    sum = 1
    while num >= 1:
        sum = sum * num
        num = num - 1
    return sum

number = factorial(factor)
print(number)

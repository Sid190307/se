
# Simple calculator using match-case

i = int(input("Enter the number 1: "))
j = int(input("Enter the number 2: "))

choice = input("Enter the operation (+, -, *, /): ")

match choice:
    case '+':
        print(i + j)
    case '-':
        print(i - j)
    case '*':
        print(i * j)
    case '/':
        print(i / j)
    case _:
        print("Invalid operation")

Output:

Input/Output


input	Actual Output
I=2,j=3, choice=’+’	5
I=2,j=3, choice=’-’	-1
I=2,j=3, choice=’*’	6
I=6,j=3, choice=’/’	2


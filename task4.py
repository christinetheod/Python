#This function adds two numbers
def addition(x,  y):
   return (x + y)

# This function subtracts two numbers
def subtract(x,  y):
    return (x - y)

# This function multiplies two numbers
def multiply(x,  y):
   return (x * y)

# This function divides two numbers
def divide(x,  y):
   return (x / y)

# Take input from the user 
choice = input("dwse tin pra3i se morfi:number1 plus/minus/times/divice number2")

n = choice.rfind(" ")
number2 = choice[n+1:] 
fisrtand = choice[:n]
m = fisrtand.rfind(" ")
act = fisrtand[m +1:]
number1 = fisrtand[:m]


if number1=='zero':
    num1=0
elif number1=='one':
    num1=1
elif number1=='two':
    num1=2
elif number1=='three':
    num1=3
elif number1=='four':
    num1=4
elif number1=='five':
    num1=5
elif number1=='six':
    num1=6
elif number1=='seven':
    num1=7
elif number1=='eight':
    num1=8
elif number1=='nine':
    num1=9

if number2=='zero':
    num2=0
elif number2=='one':
    num2=1
elif number2=='two':
    num2=2
elif number1=='three':
    num2=3
elif number2=='four':
    num2=4
elif number2=='five':
    num2=5
elif number2=='six':
    num2=6
elif number2=='seven':
    num2=7
elif number2=='eight':
    num2=8
elif number2=='nine':
    num2=9

if act == 'plus':
   print (addition(num1, num2))

elif act == 'minus':
   print(subtract(num1, num2))

elif act == 'times':
   print(multiply(num1,num2))

elif act == 'divide':
    print(divide(num1, num2))
else:
   print("Invalid input")





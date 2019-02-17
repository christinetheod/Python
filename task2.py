def factor(number):
    if number==1:
        return []
    b = 2
    while b <= number :
        while not number % b:
            return [b] + factor(number // b)
        b += 1
number = int( input ("Give me a number"))
print ("Result: ", factor(number)) 

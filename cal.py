a = int(input("enter a number\n"))

b = int(input("enter another number\n"))

print("1.Addittion\n 2.Substraction\n 3.Multiplication\n 4.Division\n")

ch = input("enter a choice\n")

def addition(num1 , num2):

    z =(num1 + num2)

    return z


if ch == 1:
    print("the addition of them number is" , addition(a,b))

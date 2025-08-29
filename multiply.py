a=int(input("Enter  a number"))
b=int(input("Enter second number"))
print("What do you want to do?")
print("1. Add")
print("2. subtarction")
print("3. Multiply")
d=int(input("Submit"))
if d==1:
    c=a+b
    print("The Sum is ", c)
elif d==2:
    c=a-b
    print("The Subtraction is ", c)
elif d==3:
    c=a*b
    print("The Multiplication  is ", c)
else:
    print("Wrong invalid number")

#Calculator



num1=int(input("Enter a value:"))
num2=int(input("Enter a value:"))
opr=input("Enter the opr:")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid input...")
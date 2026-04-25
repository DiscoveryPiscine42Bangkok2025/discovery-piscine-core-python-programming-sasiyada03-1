num1=int(input("Enter the first number:"))
num2=int(input("Enter the second numbeer:"))
result= num1*num2
print(f"{num1}*{num2}={result}")
if result >0:
    print("The result is positive")
elif result <0:
    print("the result is negative")
else:
    print("The result is zero")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    ans = a / b
    print(ans)
except Exception as e:
    print(e)
finally:
    print("Code executed.")
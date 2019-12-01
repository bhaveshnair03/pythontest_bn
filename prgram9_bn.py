x=int(input("Enter the number:"))
if (x/10 == 0):
    print("00")
elif x < 10 or x > 99:
    print("Wrong value")
else:
    a=x%10
    b=int(x/10)
    print(a,b)

a=int(input("Enter a Number"))
def fac(a):
    Mul=1
    for i in range(1,a+1):
        Mul*=i
    return Mul
print("Factorial of ",a, "is :",fac(a))

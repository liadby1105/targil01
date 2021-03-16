def exponent(x:float):
    num1=1
    num2=1
    num_total=0.0
    for i in range(0,100):
        num1=1
        num2=1
        for u in range(0,i):
            num1=num1*x
        for j in range(1,i+1):
            num2=num2*j
        num_total=num_total+(num1/num2)
    return(num_total)

def ln(x:float):
    num3=0
    if x<=0:
        return(0)
    for i in range(0,100):
        num3=num3+2*((x-exponent(num3))/(x+exponent(num3)))
    return(num3)


def XtimesY(x:float,y:float):
    num=exponent(y*ln(x))
    if (x<=0):
        return(0)
    else:
        return(num)


def sqrt(x:float,y:float):
    num=XtimesY(y,1/x)
    return(num)


def calculate(x:float):
    if x==0:
        return(0)
    num=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    num = float('%0.6f' % num)
    return(num)
'''
x = input('enter a num : ')
print(calculate(float(x)))

print(XtimesY(-2,2))
print(XtimesY(-2.2, -2))
print(sqrt(2.5, 4))
print(exponent(2.5))
print(ln(1.5))
print(calculate(1))
'''
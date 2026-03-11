# Simple interest calculator: SI = (P × R × T)/100. Take principal, rate, and time as input.
p = float(input("enter the principle amount: "))
r = float(input("enter the rate of interest: "))
t = float(input("enter the time period:   "))
SI=(p*r*t)/100
print("simple interest is: ",SI)
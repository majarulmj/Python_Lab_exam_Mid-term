import cmath
a=int(input("enter value for a "))
b=int(input("enter value for b "))
c=int(input("enter value for c "))
# discriminant formulae
d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print("the root value are ",root1,"and",root2)
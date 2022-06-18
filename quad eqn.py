def quad():
    x1 = (-b-pow((b*b-4*a*c),0.5))/2*a
    x2 = (-b+pow((b*b-4*a*c),0.5))/2*a
    print("The value of the roots of the quadratic equation is",x1)
    print("and",x2)
repeat=1
while repeat==1:
    a = int(input("\nEnter the value of the coefficient of x sq."))
    b = int(input("Enter the value of the coefficient of x"))
    c = int(input("Enter the value of the constant"))
    quad()

    repeat=int(input("\nenter 1 to make another calculation else press 0\n"))
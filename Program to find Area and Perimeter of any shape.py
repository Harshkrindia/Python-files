"""Program To find the area and Perimeter of a rictangle or a squae or a equilateral triangle
or a circle"""
a=5982
Rictangle=1
Square=2
Triangle=3
Circle=4
b=int(input("Enter password :- "))
if b==a:
    print("MADE BY PRASHANT KUMAR")
    print("This is a program to calculate perimeter and area of a shape")
    c=int(input("Plese enter number for the shape to calculate it's area and perimeter [Type Rictangle=1 , Square=2 , Triangle=3 , Circle=4] :- "))
    if c==Rictangle:
        d=int(input("Enter first mesurement for the rictangle :- "))
        e=int(input("Enter second mesurement for the rictangle :- "))
        if d==e:
            print("You entered the measurement for a square")
            print("It's perimeter=",d*4)
            print("It's area=",d**2)
            print("Thank You for using this program")
        elif d>e:
            print("Length of the rictangle=",d)
            print("Breadth of the rictangle=",e)
            print("So,")
            print("It's perimeter=",2*(d+e))
            print("It's area=",d*e)
            print("Thank You for using this program")
        else:
            print("Length of the rictangle=",e)
            print("Breadth of the rictangle=",d)
            print("So,")
            print("It's perimeter=",2*(d+e))
            print("It's area=",d*e)
            print("Thank You for using this program")
    elif c==Square:
        f=int(input("Enter mesurement for the square :- "))
        print("It's perimeter=",f*4)
        print("It's area=",f**2)
        print("Thank You for using this program")
    elif c==Triangle:
        g=int(input("Enter the length for the base of the equilateral triangle:- "))
        print("It's perimeter=",3*g)
        print("It's area=",(g**2)/2)
        print("Thank You for using this program")
    elif c==Circle:
        h=int(input("Enter the radius of the circle:- "))
        print("It's circumfrence=",2*3.14*h)
        print("It's area=",3.14*h**2)
        print("Thank You for using this program")
    else:
        print ("Try again wrrite like those in beacket")
else:
    print("Password incorrect")

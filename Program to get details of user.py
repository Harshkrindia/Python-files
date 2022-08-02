#Program to get details of user.
a=98765432109
School=1
Collage=2
Job=3
Other=4
b=int(input("Enter password :-"))
if a==b:
    print("Hello!!!",'\n')
    c=input("Plese enter your name :-")
    print(c,"hello")
    d=int(input("Are you in [School=1,Collage=2,Job=3,Other=4] :-"))
    if School==d:
        e=input("Enter school name :-")
        f=input("Enter your class :-")
        print(c,'\n',f,'\n',e)
        print("Thank","you")
        print("Thank",'\t',"you")
        print("Thank",'\n',"you")
        print ("Thank you for using this progeam")
    elif Collage==d:
        g=input("Enter for which subject :-")
        print(c,'\n'"Studies",g)
        print("Thank","you")
        print("Thank",'\t',"you")
        print("Thank",'\n',"you")
        print ("Thank you for using this progeam")
    elif Job==d:
        h=input("Enter compeny name :-")
        print(c,'\n'"Works for"'\n'"compeny :-",h)
        print("Thank","you")
        print("Thank",'\t',"you")
        print("Thank",'\n',"you")
        print ("Thank you for using this progeam")
    elif Other==d:
        i=input("What do you do then")
        print(c,'\n'"You do :-",i)
        print("Thank","you")
        print("Thank",'\t',"you")
        print("Thank",'\n',"you")
        print ("Thank you for using this progeam")
    else:
        print ("Try again wrrite like those in beacket")
else:
    print("Password incorect")

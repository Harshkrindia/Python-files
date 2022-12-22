#It will generate a report card of the user
name = input("Enter you Beautiful Name: ")
cs = input("Enter your class and section: ")
eng = float(input("Enter your English Marks: "))
hin = float(input("Enter your Hindi Marks: "))
maths = float(input("Enter your Maths Marks: "))
sc = float(input("Enter your Science Marks: "))
sst = float(input("Enter your Social studies Marks: "))

total = eng + hin + maths + sc + sst
perc = total/5
if perc >= 90:
    grade = ("A")
elif perc >= 80:
    grade = ("B")
elif perc >=70:
    grade = ("C")
elif perc >=60:
    grade = ("D")
elif perc >=50:
    grade = ("E")
else:
    grade = ("F")
if perc >= 40:
    status = ("Pass")
else:
    status = ("Fail")
print("")
print("*************************************")
print('\t', "Your Report card")
print("_____________________________________")
print("")
print("Name - ",name)
print("Class & Section - ",cs)
print("Your scored",total,"out of 500")
print("Percentage -",perc)
print("Grade -",grade)
print("Status -",status)

print("_____________________________________")
print("Thank You! Have a Nice Day")

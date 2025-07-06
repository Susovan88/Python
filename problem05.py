a1=int(input("enter a number : "))
a2=int(input("enter a number : "))
a3=int(input("enter a number : "))
a4=int(input("enter a number : "))

if(a1>a2 and a1>a3 and a1>a4):
    print("greater value is - ",a1)
elif(a2>a1 and a2>a3 and a1>a4):
    print("greater value is - ",a2)
elif(a3>a1 and a3>a2 and a1>a4):
    print("greater value is - ",a3)
else:
    print("greater value is - ",a4)

## exam marks
m1=int(input("Enter marks : "))
m2=int(input("Enter marks : "))
m3=int(input("Enter marks : "))
total_marks=(m1+m2+m3)/3
total_percentage=(100*total_marks/300)

if(total_marks>90 and total_marks<100):
    print("Gread -> A")
if(total_marks>80 and total_marks<90):
    print("Gread -> B")
if(total_marks>70 and total_marks<80):
    print("Gread -> C")
if(total_marks>60 and total_marks<70):
    print("Gread -> D")
if(total_marks>50 and total_marks<60):
    print("Gread -> E")
if(total_marks>40 and total_marks<50):
    print("Gread -> F")


if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("Total percentage is - ",total_percentage," -> You are pass!!!")
else:
    print("Total percentage is - ",total_percentage," -> Fail. Try again next Year")


## spam message
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

msg=input("Enter your message : ")

if(p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print("This commment is a spam message.")
else:
    print("This comment is not a spam")


## problem 06
l1=["pupai","mimi","pikai","susovan","taniya"]
name=input("enter you name : ")
if(name.lower() in l1):
    print("You are selecter.")
else:
    print("not selected")
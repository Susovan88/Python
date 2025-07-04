n=int(input("Enter age : "))

if(n>=18 and n<=50):
    print("good age -> selected!")
    print("good for you")
elif(n<0):
    print("are you made ?? why your age is -ve???")
elif(n>=51):
    print("age is to high to apply...")
else:
    print("so sad not selected for this jobbbbbb")

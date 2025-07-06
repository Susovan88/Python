def avg(a,b,c):
    a=(a+b+c)/3
    return a

def goodDay(name,date,ending="Thank You"):
    print(f"Hello {name}. Good morning ! ")
    print(f" Today date is {date}. Happpy Birthday!!!")
    print(f" {name} says -> {ending}")

def factorial(n): # recursion 
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)


a=avg(8,8,7)
print(f"avg is {a}")
b=factorial(5)
print("factorial is - ",b)
goodDay("susovan","24 april","Thank You for wishing me")
goodDay("taniya","14 august")
goodDay("mimi","25 august","Thank you so much!!!")


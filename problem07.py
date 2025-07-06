for i in range(1,11):
    print("7 * ",i," = ",7*i)

l1=["susovan","pupai","suchismita","taniya","mimi","sovan","sam","pinki"]
for i in l1:
    if(i.startswith("s")):
        print(f"hello {i}. you are in.")
    else:
        print(f"{i} not in. go back.")


n=int(input("enter a number: "))
for i in range(2,n):
    if(n%i==0):
        print("this is not a prime number.")
        break
else:
    print("this is a prime number.")

i=0
sum=0
while(i<=n):
    sum+=i
    i+=1
else:
    print(f"sum is {sum}")

pro=1
for i in range(1,n+1):
    pro*=i
else:
    print(f"factorial of {n} is -{pro}")


'''
n=3 ->
  *
 ***
***** 
n=4 ->
*
**
***
****

*****
*   *
*   *
*   *
****
'''
for i in range(1,n+1):
    print(" "*(n-i),end="")    
    print("*"*(2*i-1),end="")
    print("")

for i in range(1,n+1):
    print("*"*i,end="")
    print("")

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")


for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")


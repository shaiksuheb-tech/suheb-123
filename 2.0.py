print("Start the program:  ")
a = int(input("Enter the even number:  "))
b = int(input("Enter the odd number: "))
c = a+b
c = str(c)
print( a+b,a-b,a*b,a/b,a%b)


n = 5
for i in range(1,n+1):
    pattern = "*" *i
    print(pattern)

n = 5
for i in range (n,0,-1):
    pattern = "*" *i
    print(pattern)

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


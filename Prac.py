print("SHAIK MOHAMMAD SUHEB")
a = str(628)
b = str(19)
c = str(13)
d = str(986)
print(a+b+c+d)
num1 = 5
num2 = 0.5
num3 = 5+1j

print(type(num1),type(num2),type(num3))

num1 = str(num1)
print(type(num1))

a = "Vijay devarakonda"
b = 32
print("{} age is {} ".format(a,b))


a = "Vijay "
b = 39
print(f"{a} age is {b} ")

print(15<8 and 4>9)          # bitwise operator
print(15>8 or 4<9)
print(not(4>9))

a =  45                 # assignment operators
a += 10
print(a)


a  = 21
b = a            # identity operators
c = {1,2,3}
print(a is c)
print(a is b)

print(id(a))
print(id(b))
print(id(c))

# problems practice till identity operators
#1
name = "Kiran"
age = 34
height = 6.2
print("{} age is {} and his height is {}".format(name,age,height))

#2
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = a + b
print("The sum of {} and {} is : ".format(a,b),result)

#3
a = float(input("Enter the lenght: "))
b = float(input("Enter the width: "))
p = 2*(a+b)
area = a*b
print("The perimeter is: ",p)
print("The area  is: ",area)

a = "h" in "suheb"
print(a)
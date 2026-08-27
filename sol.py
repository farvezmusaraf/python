"""a =float(input("Enter a value: "))
b =float(input("Enter b value: "))
operator =input("Enter the operator(+,-,*,/,%): ")
if operator =="+":
    print(a+b)
elif operator =="-":
    print(a-b)    
elif operator =="-":
    print(a-b)
elif operator =="*":
    print(a*b)
elif operator =="/":
    print(a/b)
elif operator =="%":           
    print(a%b)
else:
    print("Invalid Operator")"""
"""b = int(input("Enter b value: "))
if b>0 and b%2 ==0:
    print("Positive Even Number")
elif b<0 and b%2 ==0:
    print("Negative Even Number")
elif b>0 and b%2 !=0:
    print("Positive Odd Number")   
elif b ==0:
    print("Zero")
else:
    print("Negative Odd Number")"""
"""a,b =input().split(",")
print(a,b)"""
"""a = input()
b = input()
c = input()
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")   
elif c>a and c>b:
    print(c,"is greater")"""
"""a =input()
b =input()
temp = a
a = b
b = temp
print(a)
print(b)"""
"""a = 10
a += 10
b = a
print(b)"""
"""attempts =1
while attempts<=3:
    a = int(input("Enter your pincode: "))
    if a==2007:
        print("__Access Guaranted!__")  
        break
    else:
        print("incorrect password!!!!")  
    attempts +=1  
if attempts == 4:
    print("-------attempts over--------")"""
"""marks = 0
for i in range(5):
    a =int(input("Enter ur marks: "))
    marks+=a
average = marks/5
print("Total Marks:",marks)
print("Average:",average)
if marks>= 90:
    print("Grade 'A' ")
elif marks >=80 and marks>= 70:
    print("Grade 'B' ") 
elif marks>=70 and marks>= 60:
    print("Grade 'c' ")
elif marks >=60 and marks>= 40:
    print("Grade 'D' ")
else:
    print("-----FAIL-----")"""
"""n =int(input())
d = n%2
if d ==0 and 2<=n<=5:
    print("Not Weird")
elif d == 0 and 6<=n<=20:
    print("Weird")  
elif d == 0 and n>20:
    print("Not Weird") 
else:
    print("Weird")"""

#Multiplication Table using(for loop):
#1 to 5 Tables:
"""for i in range(1,6):
    for j in range(1,11):
        print(f"{i} X {j} ={i * j}")"""

#printing 1 to n numbers:
"""a = 0
while a>=0:
    a += 1 #it will adds number with previous number until condition will satisfy 
    print(a)
    if a == 20:
       break """

#printing numbers from down to n numbers
"""a = 1
b = int(input(" Enter a number"))
while a<=b:
    print(b) 
    b -=a"""

"""a = 1
b = int(input("Enter a number"))
for i in range(b):
    b -=a
    print(b)"""

"""a = int(input("Enter a no."))
for i in range(0,a+1):
    print(i)"""

#Sum of  all numbers upto the given input() number
"""a =int(input("enter"))
b = 0
total = 0
while a>=b:
    total += b
    b += 1
print(total)"""  

#Even numbers:
"""a =int(input("enter"))
b = 2
while a>=b:
    print(b)
    b += 2"""
# (Even no. or odd)Using Conditional Statements.
"""a = int(input("Enter"))
b = 1
while a >= b:
    if  b % 2 == 0:
        b += 1 
        continue  
    print(b)
    b += 1"""


"""for i in  range(1,5):
    for j in range(i):
         print(i , end=" ")
    print()"""

#factorila of a number:-
"""n = int(input())
factorial = 1
while n >0:
    factorial *= n
    n -= 1
print(factorial)"""

#counting even and odd numbers:-
"""a = int(input("Enter a number: "))
b = 1
counte = 0
counto = 0
while a>=b:
    if b % 2 == 0:
        counte = counte + 1
    else:
        counto += 1    
    b += 1       
        
print("Even",counte)
print("odd",counto)"""


#Greatest of 5 numbers:-
"""greater = int(input("Enter a number: "))
count = 0
while count < 5 :
    n = int(input("Enter ur number: "))
    if n > greater:
        greater = n
    count += 1
print(greater)"""   

            



    
        
    

    



    
    








          
            






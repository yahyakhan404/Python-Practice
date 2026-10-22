a = "enter the first number"
b = "enter the second number"
opr ="select operation you want to perform [+,-,*,/]"
if opr == "+":
    print("yoyr ans is",a+b)
number =  int(input("enter the numer"))
if number>=1:
    print("number is positive")
elif number<0:
    print("number is negative")
else:
    print("number is zero")
passs = input("enter your password")
if len(passs)>=8:
    print("strong pass ")
else:
    print("weak pass")
age = int(input("eter your age"))
if age>=18:
    print("you are adult")
elif age>=13 and age<=17:
    print("you are teanager")
else:
    print("you are child1")
username = input("enter you username")
if username == "admin":
    print("welcome")
elif  username=="guest11123":
    print("welcom guest")
else:
    print("invalid")
90–100 → Excellent
75–89  → Very Good
50–74  → Good
40–49  → Pass
Below 40 → Fail
grade = int(input("enter your grade"))
if grade>=90 and grade<=100:
    print("excellent")
elif grade>=75 and grade<=89:
    print("v.good")
elif grade>=50 and grade<=74 :
    print("v.good")
elif grade>40 and grade<=49:
    print("v.good")
elif grade<=40 and grade==40:
    print("fail")
else:
    print("put grade between 1-100")
Write a program that asks for a number and prints:

Positive and even → Positive Even
Positive and odd → Positive Odd
Negative → Negative
Zero → Zero

Use if / elif / else and the % operator.
numer = int(input("enter number"))
if numer>=0 and numer%2:
    print("numer is positive and even")
elif numer<0:
    print("num is neg")
elif numer==0:
    print("numer is 0")
else:
    print("odd")
Write a program that asks for a number and checks whether it is divisible by both 3 and 5.
number = int(input('enter the number '))
if number%3 == 0 and number%5 == 0:
    print("the number is divisible by both")
else:
    print("not divisible by both")
Write a program that asks for a person's age and checks:

Age 18–60 → Eligible to work
Otherwise → Not eligible to workage 
age = int(input("enter the age"))
if age>=18 and age<=60:
    print("eligible to work")
else:
    print("not eligib;e to work")

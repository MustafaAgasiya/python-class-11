#Q1
num = int(input("enter the num "))
if num > 0 :
    print("number is positive")
else :
    print("number is negative")


#Q2
num = int(input("enter the num "))
if num%2==0 :
    print("number is even")
else :
    print("number is odd")


#Q3
num1=int(input("enter the num "))
num2=int(input("enter the num2 "))
if num1 > num2 :
    print("num1")
else :
    print("num2")


#Q4
num1=int(input("enter the num "))
num2=int(input("enter the num "))
c = num1 + num2
print(num1+num2)
if c%2==0 :
    print("number is even")
else :
    print("number is odd")


#Q5
num1=int(input("enter the num "))
num2=int(input("enter the num "))
num3=int(input("enter the num "))
percent=(num1+num2+num3)/3
if percent <=50:
    print("above 50")
else :
    print("below 50")


#Q6
score=int(input("enter the score"))
if score >=5 :
    print("pass")
else :
    print("fail")

#Q7
year=int(input("enter the year"))
if year%4==0 :
    print("it is leap year")
else :
    print("it is not a leap year")


#Q9
num1=int(input("enter the num "))
num2=int(input("enter the num "))
operator=input("enter the operator+,-,*,/")
if operator == "+" :
    print(num1+num2)
elif operator == "-" :
    print(num1-num2)
elif operator == "*" :
    print(num1*num2)
elif operator == "/" :
    print(num1/num2)
else :
    print("not valid")
    

#Q10
hour=int(input("enter the hour "))
if hour >=5 and hour <=11 :
    print("good morning")
elif hour >=12 and hour <=17 :
    print("good afternoon")
else :
    print("good evening")


#Q11
income=int(input("enter the income "))
if income <50000 :
    tax=income*5/100
    print(tax)
elif income >=50000 and income <=100000 :
    tax=income*10/100
    print(tax)
else :
    tax=income*15/100
    print(tax)


#Q8
num1=int(input("enter the num "))
num2=int(input("enter the num "))
a= num1*num2
if num1==num2 :
    print("equal")
else :
    print("not equal")


#Q12
num1=int(input("enter the bill amount "))
level=input("enter your level ")
if level == "basic" :
    amt = num1 - (num1*5/100)
    print(amt)
elif level == "premium" :
    amt = num1 - (num1*10/100)
    print(amt)
else :
    amt = num1 - (num1*15/100)
    print(amt)
    




#homework1
age = int(input("please input your age here: "))
if age <= 12:
    print("your are a kid")
elif age <= 19:
    print("you are an teenager")
elif age <= 59:
    print("you are an adult")
else:
    print("you are a senior")
#homework2
num = int(input("enter a number: "))
if num < 0:
    print("negative")
elif num == 0:
    print("zero")
elif num < 100:
    print("small number")
else:
    print("big number")
#homework3
grade = int(input("please input your grade: "))
if grade >= 90:
    print("you got an A")
elif grade >= 80:
    print("you got a B")
elif grade >= 70:
    print("you got a C")
elif grade >= 60:
    print("you got a D")
else:
    print("you got an F")
#homework4
Num = int(input("please input a number 1-7: "))
if Num == 1:
    print("Monday")
elif Num == 2:
    print("Tuesday")
elif Num == 3:
    print("Wednesday")
elif Num == 4:
    print("Thursday")
elif Num == 5:
    print("Friday")
elif Num == 6:
    print("Saturday")
elif Num == 7:
    print("Sunday")
#homework5
temperature = int(input("please input todays temperature: "))
if temperature < 0:
    print("its really cold")
elif temperature >= 0:
    print("its cool")
elif temperature >= 16:
    print("its warm today")
elif temperature >= 31:
    print("its hot")
else:
    print("its super hot")

#1 Adult and student

age=int(input("How old are you?: "))
student_status=input("are you a student? write True or False ")
adult_and_student=(age>=18 and student_status)
print(adult_and_student)
print(type(age))

#2 double filter

num1=float(input("First number: "))
num2=float(input("Second number: "))
both_positive=(num1>=0 and num2>=0)
more_than_100=(num1>100 or num2>100)

print(both_positive)
print(more_than_100)

#3number zone

number=int(input("Enter any number: "))
in_between=(number>0 and number<50)
is_negative=(number>=0)
print(in_between)
print(is_negative)

#4 age and password

age=int(input("How old are you?: "))
user_password=input("Enter your password: ")
password="admin123"
has_access=(age>=18 and password==user_password)
print(has_access)

#5 average exam

number1=float(input())
number2=float(input())
number3=float(input())

average=((number1+number2+number3)/3)
average_validation=(average>60 and number1>=0 and number2>=0 and number3>=0)
print(average_validation)
print(type(average_validation))

#6 speed control

speed=int(input("enter the speed: "))
speed_control=(speed>120 or speed<0)
print("speed violation: " + str(speed_control))

#7 height and weight 

height=float(input("how tall are you?: "))
weight=float(input("What's your weight?: "))
height_meters=(height/100)
validation=(height_meters>1.70 and weight<90)
validation2=(height_meters<1.50 or weight>120)
print(validation)
print(validation2)

#8 number character 2.0

numberX=int(input())
even=(numberX%2==0)
odd=(numberX%2!=0)
even_and_positive=(even and numberX>0)
odd_and_negative=(odd and numberX<0)

print(even_and_positive)
print(odd_and_negative)

#9 type detector

numberY=input()
print(type(numberY))
numberY_float=float(numberY)
print(type(numberY_float))
positive_under100=(numberY_float>0 and numberY_float<100)
print(positive_under100)

#10 access rules

user_age=int(input("How old are you?: "))
user_balance=float(input("What's your balance?: "))
VIP_status=input("are you VIP? True or False: ")

has_access=((user_age>=18 and user_balance>=100)or VIP_status==True)
print(has_access)
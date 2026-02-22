#1

# odd=0
# even=0

# for i in range(5):
#     n=int(input("Enter number: "))
#     if n%2==0:
#         even+=1
#     else:
#         odd+=1
# print(odd, even)

#2

# num=int(input("Enter number: "))
# sum=0

# for i in range(0, num+1, 2):
#     sum+=i
# print(sum)

#3

# secret=8
# user_input=int(input("Enter number: "))
# if user_input!=secret:
#     print("try again")
# else:
#     print("correct")

#4


# sum=0

# for i in range(3):
#     num=int(input())
#     sum+=num
# if (sum/3)>50:
#     print("Passed")
# else:
#     print("failed")


#5

# for i in range(1, 20):
#     if i%3==0:
#         print("Fizz")
#     else:
#         print(i)


#6

# num=int(input("Enter any positive number: "))
# while num<0:
#     print("error, negative number")
#     num=int(input("Try entering positive number"))
# print("Correct")

#7

# even=0
# odd=0
# for i in range(6):
#     num=int(input("Enter number: "))
#     if num%2==0:
#         even+=1
#     else:
#         odd+=1
# print(odd, even)

#8

max_num=int(input("enter first number: "))
for i in range(4):
    num=int(input("Enter next number"))
    if num>max_num:
        max_num=num
print("biggest number is: ", max_num)

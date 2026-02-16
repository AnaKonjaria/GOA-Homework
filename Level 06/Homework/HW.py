#1 

# for i in range(1, 20):
#     print(i)

# #2

# for i in range(2, 50, 2):
#     print(i)

#3

# n=int(input())
# sum=0
# for i in range (1, n):
#     sum += i
# print(sum)

#4

# num=10
# while num>1:
#     print(num)
#     num=num-1

#5

# password=input('Enter the password: ')
# while password!="python123":
#     password=input("Enter the password: ")
    
# print("access granted")

#6

# numberX=int(input("Write number here: "))
# length=0
# while numberX>0:
#     numberX//=10
#     length+=1
    
# print(length)

#7

# numberY=int(input("Write number here: "))
# multiplication=1
# for i in range (1, numberY+1):
#     multiplication*=i
# print(multiplication)

#8

# word=input("Enter any word: ")
# for i in word:
#     print(i)

#9

count=0
user_input=0
numbers=float(input("Enter any number: "))
while numbers!=0:
    numbers=float(input("Enter any number: "))
    user_input+=numbers
    count+=1
    average=numbers/count
print(average)




#1

# def sum(n):
#     sum=0
#     for num in range(n+1):
#         sum+=num
#     return sum
# print(sum(7))

#2

# def odd(n):
#     odd=0
#     for num in range(1, n+1, 2):
#         odd+=1
#     return odd
# print(odd(17))

#3

# def num_sum_until_0():
#     sum=0
#     n=1
#     while n!=0:
#         n=int(input("Enter num: "))
#         sum+=n
#     return sum

# print(num_sum_until_0())

# #4

# def list_elements_sum(x):
#     sum=0
#     for element in x:
#         sum+=element
#     return sum
# mylist=[1, 7, 7]
# print(list_elements_sum(mylist))

#5

# def list_of_evens(my_list):
#     evens=[]
#     for element in my_list:
#         if element%2==0:
#             evens.append(element)
#     return evens
# my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_of_evens(my_list))

#6

# def num_in_list(mylist, x):
#     count=0
#     for item in mylist:
#         if item==x:
#             count+=1
#     return count
# mylist=[1,2, 2, 3, 5, 2, 4]
# print(num_in_list(mylist, 2))

#7

# def triple_num(x):
#     return x**3
# print(triple_num(7))

#8

def less(x, y):
    if x<y:
        return x
    else:
        return y
print(less(9, 2))
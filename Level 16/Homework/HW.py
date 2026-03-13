#1

# def create_array(n):
#     res=[]
#     i=1
#     while i<=n:
#         res+=[i]
#         i+=1
#     return res

#2

# def remove_smallest(numbers):
#     if not numbers:
#         return []
#     new_numbers=numbers.copy()
#     new_numbers.remove(min(numbers))
    
#     return new_numbers

#3

# def likes(names):
#     n=len(names)
#     if n==0:
#         return "no one likes this"
#     elif n==1:
#         return f"{names[0]} likes this"
#     elif n==2:
#         return f"{names[0]} and {names[1]} like this"
#     elif n==3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {n-2} others like this"

#4

# def count_by(x, n):
#     return[i*x for i in range(1, n+1)]

#5

# def between(a,b):
#     mylist=[]
#     for num in range(a, b+1):
#         mylist.append(num)
#     return mylist
        
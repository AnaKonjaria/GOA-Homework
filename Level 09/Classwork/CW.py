numbers=[2, 6, -8, 8, -9, 13]
positive=0
negative=0
for i in numbers:
    if i>0:
        positive+=1
    else:
        negative+=1
print(positive, negative)

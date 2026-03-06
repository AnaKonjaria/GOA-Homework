#1

# text=input("Enter sentence: ")
# print(text.upper())

#2

# text=input("Enter sentence: ")
# print(text.lower())
# print(len(text))

#3

# text=input("Enter sentence: ")
# print(text.capitalize())


#4

# text=input("Enter sentence: ")
# symbol=input("Enter a symbol: ")
# print(text.find(symbol))


#5

# text=input("Enter sentence: ")
# text.lower()
# print(text.find('python'))

#6

# def how_many_symbols(text, symbol):
#     count=0
#     for char in text:
#         if char==symbol:
#             count+=1
#     return count

# print(how_many_symbols("ana, ana , ana", "a"))


#7

# def capitals(text):
#     uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     count = 0
#     for char in text:
#         if char in uppercase_letters:
#             count+=1

#     return count

# print(capitals("sdhaWdbsFsfsA"))

#8

def word_in_sentence(word, sentence):
    if word in sentence:
        return True
print(word_in_sentence("cat", "My dog is 10 years old"))
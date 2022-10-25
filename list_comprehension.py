# List comprihence is a way to compress our code in one single line rather than multiple lines present in there


# fruits=["apples","Bananas","kiwi","Pineapples","Mango"]
# newfruit=[]
#
# #General way/process of list comprehension
#
# for x in fruits:
#     if "a" in x:
#         newfruit.append(x)
#         #print(newfruit)
#
# print(newfruit)
#
#
# for x in fruits:
#     if "i" in x:
#         newfruit.append(x)
#         #print(newfruit)
# 
# print(newfruit)


# Main function or proper way to write for loop in list comprihension
fruits = ["apples", "Bananas", "kiwi", "Pineapples", "Mango"]

# To print word which contains i
newfruit = [x for x in fruits if "i" in x]

# To print word which contains a
# newfruit=[x for x in fruits if "a" in x]
print(newfruit)

# printing without any one word like we test here to Bananas
fal = ["apples", "Bananas", "kiwi", "Pineapples", "Mango"]
newfal = [y for y in fal if y != "Bananas"]
print(newfal)

# To print all fal list values in new list newfru
newfru = [z for z in fal]
print(newfru)

# to print numbers
num1 = [a for a in range(10)]
print(num1)
# to print number less than 6
num = [a for a in range(10) if a <= 6]
print(num)

# To print alfabets in upper case
str = [b.upper() for b in fal]
print(str)

# To print alfabets in lower case
stri = [b.lower() for b in fal]
print(stri)

# If we wanna replace any word like here we are doing with mango
rep = [c if c != "Mango" else "Orange" for c in fal]
print(rep)

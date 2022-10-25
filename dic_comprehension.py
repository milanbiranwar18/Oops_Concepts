# without dic comprehension
dict1 = {}
for n in range(10):
    dict1[n] = n*2
print(dict1)


# with dic comprehension
dict2 = {n:n*2 for n in range(10)}
print(dict2)

# without dic comprehension
dict3 = {}
for n in range(10):
    if n % 2 == 0:
        dict3[n] = n*2
print(dict3)


# with dic comprehension
dict4 = {n:n*2 for n in range(10) if n%2==0}
print(dict4)


# without dic comprehension
dict5 = {}
for n in range(10):
    if n % 2 == 0:
        if n%3==0:
         dict5[n] = n*2
print(dict5)


# with dic comprehension
dict6 = {n:n*2 for n in range(10) if n%2==0  if n%3==0}
print(dict6)


# without dic comprehension
dict7 = {}
for n in range(10):
    if n % 2 == 0:
        dict7[n] = n
    else:
        dict7[n] = "Invalid"
print(dict7)


# with dic comprehension
dict8 = {n:(n if n%2==0 else 'Invalid') for n in range(10)}
print(dict8)


# list of tuple changing/converting to dictionary

lst = [(101, "milan"), (102, "Raj")]

dict9 = {k:v for k,v in lst}

print(dict9)
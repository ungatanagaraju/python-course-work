''''
>8
u
l
s
d

 

password = input("Enter the password: ")

if len(password)>=8:
    status = set()
    for i in password :
        if i.isupper():
            status.add('u')
        elif i.islower():
            status.add('l')
        elif i.isdigit():
            status.add('d')
        else:
            status.add('s')
    if len(status)==4:
        print("Strong password")
    else:
        print("weak password")
else:
    print("weak password")

'''

products={
    1:{"name":"Rice","price":60},
    2:{"name":"wheat flour","price":45},
    3:{"name":"sugar","price":40},
    4:{"name":"Milk","price":25},
    5:{"name":"Eggs","price":70},
    6:{"name":"Cooking oil","price":130},
    7:{"name":"Tea Powder","price":90},
    8:{"name":"Salt","price":20},
    9:{"name":"Bread","price":30},
    10:{"name":"Soap","price":25}
    }
print('------Welcome to Grocery store---')
print('Here are the available product:')


    

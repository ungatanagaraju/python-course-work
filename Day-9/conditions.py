'''
Simple if (only one condition)
eg: mobile phone charger, product discount, best seller

if-else condition
eg: resume, shortlist, online exam time, subscription
 
if-elif-else condition
eg: rapido, temp, rating, face reg, online payment,

Nested if condition
eg: password-strong, order status


if condition:
   #stmts

charger = int(input("Enter the charging:"))
if charger<=20:
    print("charge the phone or turn on power saving mode")

'''

'''
products = {
          1:{'name':'bread','discount':10},
          2:{'name':'sugar','discount':0},
          3:{'name':'jam','discount':5},
          4:{'name':'butter','discount':0},
          }
print(products)

index = int(input("Enter the index: "))
if product[index]['discount']:
    print(f'{products[index]["name"]}has discount').


#if else

jd ={'python','mysql','javascript','flask'}

skills = set(input("Enter the skills: ").split())

if jd == skills:
    print("congrates!! you resume is shortlisted")
else:
    print(f"sorry,try again. you need this skills set:{jd-skills}")
    



plan = True
if plan:
    print("Ads won't run. you can watch the video without interuption")
else:
    print("Ads will run. Subscribe to youtube premium")
    
    

# Naster if

 status = input("Enter the status:")

if status=='face':
    print("unlock the mobile")
else:
    print("unlock to reg face")
    if status=='password':
        print("unlock the mobile")
    else:
        print('Incorrect Password')


#if,elif,elif

wheels = int(input("Enter the wheels:"))
if wheels== 2:
    print("your bike is on the way. please pay $50")
elif wheels == 3:
    print("your auto is on the way. please pay $150")
elif wheels == 4:
    print("your cab is on the way. please pay $200")
else:
    print("incorrect password")

''''
#Nasted
products = {
          1:{'name':'bread','discount':10},
          2:{'name':'sugar','discount':0},
          3:{'name':'jam','discount':5},
          4:{'name':'butter','discount':0},
          }








#1...10
#while loop
'''
i=20
while i>9:
    print(i)
    i=i-1

i=30
while i<51:
    print (i)
    i=i+1

i=10
while i<11:
    print(i)
    i=i+1

i=1
while i<11:
    if i==5:
        break
    print(i)
    i=i+1

i=9
while i>15:
    if i==6:
        break
    print(i)
    i=i-1
    
i=9
while i>15:
     i=i-1
     if i==6:
     continue
    print(i)

'''
i=1
while i<11:
    if i==15:
        break
    print(i)
    i=i+1
else:
    print('1..10 numbers are printed')



l=[1,0,1,2,0,0,0,7,3,4,5,6,0,0,0,0,1,2,3,4,5,6,0]

while 0 in l:
    l.remove(0)
print(l)


 

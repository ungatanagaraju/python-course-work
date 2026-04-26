pin=12345

for i in range(5):
    epin=int(input("Enter the pin:"))
    if pin==epin:
        print("Login successful")
        break
    else:
        print("Incorrect pin")
else:
    print("Try Again after 60 Seconds")

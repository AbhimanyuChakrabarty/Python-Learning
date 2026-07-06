
print("Welcome to Rollercoster Ticket COunter!")

height= int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")

    age= int(input("What is your age?"))

    if age >= 18:
        print("Adult ticket is 20rs")
        bill = 20

    elif age >= 12:
        print("Child ticket is 15rs")
        bill = 15

    else:
        print("Youth tickets are 10rs")
        bill = 10
    
    photo= input("Do you want to take a photo? Type y for Yes and n for No")
    if photo == "y": 
        bill += 5
    
    print(f"You gonna be paying {bill} rs")



else:
    print("You can't ride the rollercoaster!")
    



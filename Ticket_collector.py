print("Welcome to Rollercoster Ticket Counter!")

height= int(input("What is your height in cm? "))
bill = 0
if height >= 120 :
    print("You can ride the rollercoaster!")

   


    age = int(input("What is Your age? \n"))

    if age <= 12 :
        print("Child ticket is 10rs")
        bill = 10

    elif age < 18 :
         print("Youth ticket is 15rs")
         bill = 15
# If i need to incorporate logical operator for another condition
# Like poeple aged 45-55 have Mid-Life crisis, their ticket is free.
    elif age >=45 and age <= 55 :
         print("Everything is Okay!, Have a free ride, refresh yourself!")
         bill = 0

    else:
         print("Adult ticket is 20rs")
         bill = 20


    photo = input("Do you want a photo? ; It will be an extra 5rs \n type y for YES and n for NO\n")
    if photo == "y":
         bill += 5
    
    print(f"You gonna be paying {bill} rs")

else:
     print("You can't ride the rollercoaster! \n Grow Taller!") 





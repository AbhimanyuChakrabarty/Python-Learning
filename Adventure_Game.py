print('''
***********************************************************************************
------------------------WELCOME TO THE ADVENTURE GAME!------------------------------
----------Let's embark on a thrilling experience of Treasure Hunting----------------
************************************************************************************
                                   __________ 
                                  /          \      
                                 /____________\     
                                |  * * * * * * |  
                                |==============|    
                                |  $  Gold  $  |    
                                |______________|
************************************************************************************
      
''') 
print("You are standing in front of a River." \
"To continue your adventure, you must cross it." \
"Either you can 'wait' for a Boat or 'swim' across.")

choice1 = input("how do you want to cross the river? \ Type 'Swim' or 'Wait': ").lower()
if choice1 == "wait":
    print("You waited for a boat and safely crossed the river." \
        "Now you are in front of a Jungle." \
        "To continue your adventure, you must choose between 3 paths." )
    
    choice2 = input("Which path do you want to take? Type 'Left', 'Right' or 'Straight': ").lower()
    if choice2 == "left":
        print("You took the left path and found a treasure chest filled with gold! You Win!")
    elif choice2 == "right":
        print("You took the right path and Got eaten by a tiger. Game Over!")
    elif choice2 == "straight":
        print("You took the straight path and fell into a pit of snakes. Game Over!")
else:
    print("You tried to swim across the river but got attacked by a crocodile. Game Over!"
    )
    
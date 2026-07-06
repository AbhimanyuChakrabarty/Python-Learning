print("Welcome to the Tip Calculator!")

total_bill= float(input("What was the total bill? "))

tip_percentage= float(input("How much tip would you like to give? 10, 12 or 15? "))

number_of_people = float(input("How many people to split the bill? "))

final_bill = (total_bill * (tip_percentage/100)) + total_bill 
final_split = final_bill / number_of_people
final_split = round(final_split, 2)


print(f"Each person should pay: {final_split}")


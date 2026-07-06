height = float(input("Input your Height in cm: "))
weight= float(input("Input your Weight in kg: "))

convert = float(height/100)


bmi = float(weight / (convert ** 2))
print(bmi)

print("Your BMI is = " + str(round(bmi, 2 )))

if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal Weight")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")



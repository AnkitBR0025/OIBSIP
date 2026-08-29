print("---CHECK YOUR BMI(Body Mass Index)---")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in feet: "))

height_meter = height * 0.3048

bmi = weight / (height_meter ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal 👍"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese 🐘"

print(f"\nYour weight is {weight} kg and height is {round(height_meter, 2)} m.")
print("\nResult:-")
print(f"Your BMI is: {round(bmi,2)}")
print(f"Category: {category}")
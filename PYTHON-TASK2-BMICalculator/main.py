# Name:- Ankit Kumar Pandey
# Track:- Python Programming
# Task Title:- BMI Calculator


print("--- CHECK YOUR BMI (Body Mass Index) ---")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in feet: "))

    # Check for negative or zero values
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than 0.")
    else:
        # Convert height from feet to meters
        height_meter = height * 0.3048

        # Calculate BMI
        bmi = weight / (height_meter ** 2)

        # Determine BMI category
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
        print(f"Your BMI is: {round(bmi, 2)}")
        print(f"Category: {category}")

except ValueError:
    print("Error: Please enter numeric values only.")


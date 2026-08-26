print("---CHECK YOUR BMI(Body Mass Index)---")

def get_positive_number(val):
    while True:
        value = input(val).strip()

        try:
            number = float(value)
        except ValueError:
            print("That's not a valid number. \nPlease enter digits only, like 65 or 1.75.")
            continue

        if number <= 0:
            print("Value must be greater than zero. Please try again.")
            continue

        return number


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def check_category(bmi):
    if bmi < 18.5:
        return "Underweight "
    elif bmi < 25:
        return "Normal 👍"
    elif bmi < 30:
        return "Overweight "
    else:
        return "Obese 🐘"


def main():

    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in feet: ")
    
    height_meter = height * 0.3048




    bmi = calculate_bmi(weight, height_meter)
    category = check_category(bmi)
    print(f"\nYour weight is {weight} kg and height is {height} m.")
    print("\nResult:-")
    print(f"Your BMI is: {round(bmi,2)}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    # Categorize based on BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Input for weight and height
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Get the BMI category
    category = bmi_category(bmi)

    # Output BMI and Category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numeric values for weight and height.")


# Define a function
def calculate_BMI():

    weight = float(input("Enter your weight in pound: "))
    height = float(input("Enter your height in inches: "))
    BMI = (weight * 703) / (height * height)

    print(BMI)
    if BMI < 18.5:
        print("Under weight")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("Normal")
    elif BMI >= 25.0 and BMI <= 29.9:
        print("Overweight")
    else:
        print("Obesity")


# Call function

calculate_BMI()
calculate_BMI()
calculate_BMI()
calculate_BMI()
calculate_BMI()
calculate_BMI()
calculate_BMI()
calculate_BMI()
calculate_BMI()

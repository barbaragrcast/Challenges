def BMI_checker(weight, height):
    BMI = weight/(height**2)
    print(f"You BMI is {BMI}")
    if BMI < 18.5:
        print("You are underweight")
    elif BMI > 18.5 and BMI < 24.9:
        print("You have a normal weight")
    elif BMI > 25 and BMI < 29.9:
        print("You are overweight")
    elif BMI > 30:
        print("You have obesity")

menu = True
while menu == True:
    weight = input("Please enter your weight in kilograms(kg): ")
    height = input("Please enter your height in meters(m): ")
    if weight.isalpha() or height.isalpha():
        print("Error, please input a valid number")
    elif weight == "" or height == "":
        print("Error, please input a valid number")
    elif float(weight) <= 0 or float(height) <= 0:
        print("Error, please input a valid number")
    else:
        weight = float(weight)
        height = float(height)
        BMI_checker(weight, height)
        menu = False





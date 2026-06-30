name = input("enter your name:")
weight = float(input("enter your weight in kilograms:"))
height = float(input("enter your height in meter:"))

if weight <= 0 or height <= 0:
    print("Please enter valid height and weight.")
else:
    BMI = weight/(height **2)
    print(f"Your BMI is: {BMI:.2f}")
    if BMI > 0:
        if BMI<18.5:
            print(name +" , you are underweight")
        elif BMI<=24.9:
            print(name + ", you are normal weight")
        elif BMI<29.9:
            print(name + ", you are overweight")
        elif BMI<34.9:
            print(name + ", you are obese")
        elif BMI<39.9:
            print(name + ",you are severly obese")
        else:
            print(name + ",you are morbidly obese")
    else:               
        print("enter valid input")
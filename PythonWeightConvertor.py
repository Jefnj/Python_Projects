# Python Weight Convertor
weight=float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(K or P)?")
if unit == "P":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "K":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")




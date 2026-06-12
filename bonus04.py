def calculate_bmi(weight, height):
    return weight / (height * height)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


weight = float(input("Og‘irlikni kiriting kg: "))
height = float(input("Bo‘yni kiriting metrda: "))

bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)

print("BMI:", bmi)
print("Holat:", status)
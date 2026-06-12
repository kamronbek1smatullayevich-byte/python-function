def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


score = int(input("Ball kiriting: "))

grade = get_grade(score)

print("Sizning bahoyingiz:", grade)
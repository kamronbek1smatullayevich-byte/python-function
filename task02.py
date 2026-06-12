def calculate_age(birth_year, current_year):
    return current_year - birth_year


def main():
    birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
    current_year = int(input("Hozirgi yilni kiriting: "))

    age = calculate_age(birth_year, current_year)

    if age >= 18:
        print("Siz balog'atga yetgansiz")
    else:
        print("Siz balog'atga yetmagansiz")

    print(f"Sizning yoshingiz: {age}")    


main()

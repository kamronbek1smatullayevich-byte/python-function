def is_valid_phone_number(phone):
    return len(phone) == 9 and phone.isdigit()


phone = input("Telefon raqam kiriting: ")

if is_valid_phone_number(phone):
    print("Telefon raqam to‘g‘ri")
else:
    print("Telefon raqam noto‘g‘ri")
def is_strong_password(password):
    return len(password) >= 8


password = input("Parol kiriting: ")

if is_strong_password(password):
    print("Kuchli parol")
else:
    print("Kuchsiz parol")
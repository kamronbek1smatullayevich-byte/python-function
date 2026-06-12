def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


choice = input("Qaysi amal? C-F yoki F-C: ")

if choice == "C-F":
    celsius = float(input("Celsius kiriting: "))
    result = c_to_f(celsius)
    print("Fahrenheit:", result)

elif choice == "F-C":
    fahrenheit = float(input("Fahrenheit kiriting: "))
    result = f_to_c(fahrenheit)
    print("Celsius:", result)

else:
    print("Noto‘g‘ri tanlov")
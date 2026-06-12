def is_even(number):
    return number % 2 == 0

def print_even_message(number):
    if is_even(number):
        print("Bu juft son")
    else:
        print("Bu toq son")


number = int(input("Son kiriting: "))
print_even_message(number)
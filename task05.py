def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To‘g‘ri topdingiz!")
    else:
        print("Xato taxmin qildingiz")


secret = 7

guess = int(input("Sirli sonni toping: "))

result = check_guess(secret, guess)

print_result(result)
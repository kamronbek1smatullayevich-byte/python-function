def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def ask_question(question, correct_answer):
    user_answer = input(question + " ")

    if check_answer(user_answer, correct_answer):
        print("To‘g‘ri javob!")
    else:
        print("Noto‘g‘ri javob")


ask_question("Python dasturlash tilimi?", "ha")
ask_question("2 + 2 nechchi?", "4")
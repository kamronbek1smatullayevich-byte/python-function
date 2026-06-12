
def add(a, b):
    return a + b                    

def subtract(a, b):
    return a - b    

def multiply(a, b):
    return a * b    

def divide(a, b):   
    if b != 0:
        return a / b    
    else:
        return "Xato: nolga bo'lish ruxsat etilmaydi."
def main():
    num1 = float(input("Birinchi sonni kiriting: "))
    num2 = float(input("Ikkinchi sonni kiriting: "))
    operation = input("Amalni kiriting (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Xato: Noto'g'ri amal."

    print("Natija:", result)
if __name__ == "__main__":
    main()


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


while True:
    S = input("enter calculation")
    input_list = S.split()

    if len(input_list) !=3:
        print("Invalid input ")
        continue

    try:
        x = int(input_list[0])
        y = int(input_list[2])
    except ValueError:
        print("Invalid input ")
        continue

    if input_list[1] == '+':
        print(x, "+", y, "=", add(x, y))
    elif input_list[1] == '-':
        print(x, "-", y, "=", subtract(x, y))
    elif input_list[1] == '*':
        print(x, "*", y, "=", multiply(x, y))
    else:
        print("Invalid input.")

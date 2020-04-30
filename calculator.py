i = 1
while i < 10:
    print("Please enter your first value: ")
    x = float(input())
    print("Please enter your second value: ")
    y = float(input())

    print("Type 1 to:Add/ Type 2 to:Subtract/Type 3 to:Multiplicate/Type 4 to:Divide")
    answer = input()

    def add():
        print(x + y)

    def subtract():
        print(x - y)

    def multiplication():
        print(x * y)

    def division():
        print(x / y)


    if answer == "1":
        add()
    elif answer == "2":
        subtract()
    elif answer == "3":
        multiplication()
    elif answer == "4":
        division()









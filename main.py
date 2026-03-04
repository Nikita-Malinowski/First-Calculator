# Taschenrechner Projekt 

while True:

    eingabe = input("Gib eine Zahl ein oder 'exit': ")

    if eingabe == "exit":
        break

    Zahl1 = float(eingabe)
    op = input('+, -, *, /, : ')
    Zahl2 = float(input("Gib eine zweite Zahl ein!: "))

    if op == '+':
        print(Zahl1 + Zahl2)
    elif op == '-':
        print(Zahl1 - Zahl2)
    elif op == '*':
        print(Zahl1 * Zahl2)
    elif op == '/':
        print(Zahl1 / Zahl2)
    else:
        print("Falsche Eingabe")
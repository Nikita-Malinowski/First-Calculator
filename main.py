# Taschenrechner Projekt gestartet

Zahl1 = float(input("Gib eine Zahl ein!: "))
op = input('+, -, *, /, : ')
Zahl2 = float(input("Gib nochmal eine Zahl ein!: "))

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
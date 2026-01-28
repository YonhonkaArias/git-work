def Calculadora():
    print("1. suma")
    print("2. resta")

    option = input("Elige una opción (1-2)")

    num1 = float(input("Pon el primer numero:"))
    num2 = float(input("Pon el primsegundoer numero:"))

    if option == "1":
        result = num1 + num2
        print("Resultado:", result)
    elif option == "2":
        result = num1 - num2
        print("Resultado:", result)
Calculadora()
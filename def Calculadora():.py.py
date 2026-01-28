def Calculadora():
    print("1. suma")
    print("2. resta")
    print("multiplicacion")
    print("division")

    option = input("Elige una opción (1-4)")

    num1 = float(input("Pon el primer numero:"))
    num2 = float(input("Pon el primsegundoer numero:"))

    if option == "1":
        result = num1 + num2
        print("Resultado:", result)
    elif option == "2":
        result = num1 - num2
        print("Resultado:", result)
    elif option == "3":
        result = num1 * num2
        print("Resultado:", result)
    elif option == "4":
        if num2 == 0:
            print("no se puede dividir por 0")
    else:
        result = num1/num2
        print("Resultado:", result)
Calculadora()


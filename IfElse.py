nombre = str(input("Como te llamas?"))
if nombre == "Alejandra":
    print('Hola', nombre)


nombre = str(input("Dame tu nombre: "))
if nombre == "Guadalupe":
    print("hola", nombre)
else:
    print("No te conozco. ")


procesador = float(input("Cuantos megaherzios tiene su procesador?"))
ram = int(input("Cuanta memoria RAM tiene su ordenador?"))
if procesador >= 1000:
    print("Tu procesador cumple los requisitos.")
else:
    print("Tu procesador no cumple los requisitos.")
if ram >= 1024:
    print("Tienes suficiente memoria RAM.")
else:
    print("No tienes suficiente memoria RAM.")
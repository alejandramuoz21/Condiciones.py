num = int(input("Introduzca un numero"))
if num < 0:
    print(num, "es un numero negativo.")
elif num > 0:
    print(num, "es un numero positivo.")
elif num == 0:
    print(num, "no pertenece a ningun grupo.")



nombre = str(input("Como te llamas?"))
if nombre == "Ale":
    print("Hola", nombre)
elif nombre == "Lupita":
    print("Hola", nombre)
else:
    print("No te conozco. ")
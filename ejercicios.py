# Ejercicio #1

# on = "si"

# while on == "si":
#     nombre = input("Dame tu nombre: ")
#     edad = input("Dame tu edad: ")
#     genero = input("Dame tu genero: ")
#     on = input(f"{nombre} Quieres ingresar tus datos nuevamente (si/no): ")


#     print(f"Chao, {nombre}")



# Ejercicio #2

nombres =""
edad= ""
direcion =""
tel =""
correo =""
acerca =""

print(f"1.Nombres y Apellidos")
print(f"2.Direcciones")
print(f"3.Correo")
print(f"4.Edad")
print(f"5.telefono")
print(f"6.Acerca de")
print(f"7.imprimir Todo")
print(f"8.Ingresar Todo")
print(f"Quiere salir ")


while True:
   
    option = int(input(f"elige la opcion que deseas usando (1,2,3,4,5,6,7,8,9) "))

    if option == 1 :
        if nombres != "":
            print(f"estos son tus nombres {nombres}")
        else:
            nombres = input("No hay nombre registrados, ingresa un nombre: ")

    if option == 2 :
        if edad != "":
            print(f"estos son tus edades {edad}")
        else:
            edad = input("No hay edades registradas, ingresa una edad: ")

    if option == 3 :
        if direcion != "":
            print(f"estos son tus direciones {direcion}")
        else:
            direcion = input("No hay direciones registradas, ingresa una direcion: ")        

    if option == 4 :
        if correo != "":
            print(f"estos son tus correos {correo}")
        else:
            correo = input("No hay correo registrados, ingresa un correo: ")   
    if option == 5 :
        if tel != "":
            print(f"estos son tus telefonos de {tel}")
        else:
            tell = input("No hay telefono registrados, ingresa un telefono de: ")           

    if option == 6 :
        if acerca != "":
            print(f"estos son tus datos acerca de {acerca}")
        else:
            acerca = input("No hay acerca de registrados, ingresa un acerca de: ")  

    if option == 7 :
        print(f"Estos son todos tus datos: {nombres} {edad} {direcion} {correo} {tel} {acerca} ")

    if option == 8 :
        nombres = input("ingresa un nombre: ")
        edad = input("ingresa una edad: ")
        direcion = input("ingresa una direcion: ")
        correo = input("ingresa un correo: ")
        tell = input("ingresa un telefono de: ")
        acerca = input("ingresa un acerca de: ")

    if option == 9 :
        print("Chao")

        break

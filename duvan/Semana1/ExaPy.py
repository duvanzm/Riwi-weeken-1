#  Tipo de Varrialbles

int = 8
bool = True
float = 1.7
str = "Hola Mundo"
lis = [1,"duvan", 1.1, True]
tupla = ("duvan",1.1, True)
dic = {
    "nom": "duvan",
    "edad": 15,
    "hombre": True,
    "estatura": 1.78
    }
print(type(int).__name__)
print(type(bool).__name__)
print(type(float).__name__)
print(type(str).__name__)
print(type(lis).__name__)
print(type(tupla).__name__)
print(type(dic).__name__)

#  Operadores en Python

#Operadores Aritmeticos

num1 = 9
num2 = 3

# suma 
suma = num1 + num2
print(f"suma = {suma}")

# resta
resta = num1 - num2
print(f"resta = {resta}")

# multiplicacion
mult = num1 * num2
print(f"multiplicacion = {mult}")

# potencia
ptcia = num1 ** num2
print(f"potencia = {ptcia}")

# divicion
div = num1 / num2
print(f"divicion = {div}")

# divicion entera 
# me redondea el relsultado de la division a un numero entero
divInt = num1 // num2
print(f"divItn = {divInt}")

# modulo 
# el modulo me da el resto de la division 
mod = num1 % num2
print(f"modulo = {mod}")

# operadored de relacion
# < ; >; =< ; =>; ==; !=
#--------------------------


# operadores logicos
# and , or, not
#-----------------------

# condicionales 

# if
# Solo evalua una condicion inicial

if (5 > 3) :
    print(f" ejemplo if 5 es mayo que 3")

# if - else
# Evalua condiciones adicionales solo si las anteriores fueron falsal
ifElseNum1 = input("Ingresa un numero a comparar")
ifElseNum2 = input("Ingresa un numero a comparar")

if (ifElseNum1 > ifElseNum2):
    print(f"{ifElseNum1} es mayor {ifElseNum2}")
else:  
    print(f"{ifElseNum1} es menor {ifElseNum2}")

# if-elif-else
tuCalificacion = input("ingresa tu calificacion por favor") 


if tuCalificacion == 0: 
        print("Tu calificación es 0, no hay ningún premio.") 
elif tuCalificacion == 1: 
        print("Tu calificación es 1, ganas un trofeo de 100 puntos.") 
elif tuCalificacion == 2: 
        print("Tu calificación es 2, ganas un trofeo de 200 puntos.") 
elif tuCalificacion == 3: 
        print("Tu calificación es 3, ganas un trofeo de 300 puntos.") 
elif tuCalificacion == 4: 
        print("Tu calificación es 4, ganas un trofeo de 400 puntos.") 
elif tuCalificacion == 5: 
        print("Tu calificación es 5, ganas un trofeo de 500 puntos.")

else:
       print("Tu calificaion no esta en el rango valido (0-5)")   
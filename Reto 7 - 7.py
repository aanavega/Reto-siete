# Leer un numero entre 2 a 50 para evaluarle la condicion
numero = int(input("Ingrese un numero de 2 a 50: "))

# Definir la condicion para evaluar los divisores del numero ingresado
if numero >= 2 and numero <= 50:
    print("Los divisores de " +str(numero)+ " son: ")
    i = 1

# Definir si el residuo del numero entre 1 o 1+1 (asi sucesivamente) es 0
    while i <= numero:
        if numero % i == 0:
            print(i)
        i += 1

# Definir el otro caso en el que el numero ingresado esta fuera del rango
else:
    print("El numero " + str(numero) + " no esta en el rango")
# Definir la funcion para calcular los numeros primos de 1 hasta a 100
def calcularprimos(numero):
    
# Si el numero es divisible entre 2 y su raiz cuadrada, no es primo
    i = 2
    while i*i <= numero:
      if numero % i == 0:
        return False
      
# Por el contrario, si no es divisible, es primo
      i += 1
    return True

# Definir funcion para verificar si el numero es primo
def numerosprimos():
    print("Números primos del 1 al 100: ")
    num = 2

# Definir la condicion del bucle
    while num <= 100:
        if calcularprimos(num):
            print(num)
        num += 1

# Llamar funcion inicial para mostrar los numeros primos
numerosprimos()

# Definir los rangos para adivinar un numero
numerominimo = 1
numeromaximo = 100

# Definir variable de numero a adivinar 
numeroadivinar = int(input("Ingresa un número entre 1 y 100 (simulacion): "))

# Establecer la condicion del numero
if numeroadivinar > 100:
  print("El numero no esta en el rango ")

# Definir un bucle con las condiciones del numeroo 
while True:
  while True:
      suposicion = int(input("Numero entre " + str(numerominimo) + " y " + str(numeromaximo) + " para adivinar: "))
      if suposicion >= numerominimo and suposicion <= numeromaximo:
        break
      else:
        print("Los numeros no estan dentro del rango solicitado")

# Definir condicion si la adivinanza es acertada
  if suposicion == numeroadivinar:
    print("La adivinanza ha sido acertada")
    break
  elif numeroadivinar > suposicion:
    print("Muy bajo. Intente nuevamente.")
  else:
    print("Muy alto. Intenta nuevamente.")
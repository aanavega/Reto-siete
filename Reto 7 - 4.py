# Definir variables de cada pais y el año dado
poblacionA = 25
poblacionB = 18.9
año = 2022

# Definir la condicion del bucle
while poblacionA > poblacionB:
  poblacionA *= 1+0.02
  poblacionB *= 1+0.03

# Incrementar el valor del año para que complete el bucle
  año += 1
print("El año en el que la población del país B superará a la de A es: " +str(año))

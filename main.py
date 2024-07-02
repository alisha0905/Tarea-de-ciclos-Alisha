#Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.
numero = int(input("Ingrese un numero: "))
for i in range(1, numero+1):
  print(i)
  
#Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

numero = int(input("Ingrese un numero: "))
for i in range(1, numero+1):
  if i % 2 == 0:
    print(i)


#Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído

numero = int(input("Ingrese un numero: "))
for i in range(1, numero+1):
  if numero % i == 0:
    print(i)

#4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.

numero_1 = int(input("Ingrese un el primer numero: "))
numero_2 = int(input("Ingrese un el segundo numero: "))
for i in range(numero_1+1, numero_2):
  print(i)


# Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

numero_1 = int(input("Ingrese un el primer numero: "))
numero_2 = int(input("Ingrese un el segundo numero: "))
for i in range(numero_1+1, numero_2):
  if i % 10 == 4:
    print(i)

#Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos. 

numero = int(input("Ingrese un numero de tres digitos: "))
if numero <100 or numero > 999:
  print("No es un numero de tres digitos")
else:
  digito1 = numero // 100
digito2 = (numero // 10) % 10
digito3 = numero % 10

print("El primer rango es:")
for i in range(1, digito1):
  print(i)

print("El segundo rango es:")
for i in range(1, digito2):
  print(i)

print("El tercer rango es:")
for i in range(1, digito3):
  print(i)

#Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.
for i in range(1, 100):
  print(i)

#8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.

for i in range(20, 200):
  if i % 2 == 0:
    print(i)

#9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.

for i in range(25, 205):
  if i % 10 == 6:
    print(i)

#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.
numero = int(input("Ingrese un numero: "))
suma = 0
for i in range(1, numero+1):
  suma += i

print("La suma de los numeros es: ") 
print(suma)

#Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.

numero = int(input("Ingrese un numero de dos digitos: "))
if numero>99 or numero<10:
  print("El numero no tiene dos digitos")
  exit() 
else:
  digito1= numero // 10
  digito2= numero % 10
  print("El numeros entre los digitos son:")
  for i in range(min(digito1, digito2)+1, max(digito1, digito2)):
    print(i)


12#Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

numero = int(input("Ingrese un numero de tres digitos: "))
if numero <100 or numero > 999:
  print("No es un numero de tres digitos")
else:
  digito1 = numero // 100
digito2 = (numero // 10) % 10
digito3 = numero % 10

if digito1 == 1 or digito2 == 1 or digito3 == 1:
  print("El numero tiene el digito 1")
else:
  print("El numero no tiene el digito 1")


#13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.

  numero = int(input("Ingrese un numero: "))
  for i in range(1, numero+1):
    if i % 5 == 0:
      print(i )


#14. Mostrar en pantalla los primeros 20 múltiplos de 3.

  for i in range(1, 61):
    if i % 3 == 0:
      print(i)

#15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.

suma=0
for i in range(1, 61):
  if i % 3 == 0:
    suma += i

print("La suma de los primero 20 multiplos de 3 es: ")
print(suma)

#Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.

numero = int(input("Ingrese un numero: "))
suma=0
contador=0
for i in range(1, numero):
  if i % 2 == 0:
    suma += i
    contador +=1

promedio_de2= (suma/contador)

suma2=0
contador2=0
for i in range(1, numero):
  if i % 5 == 0:
    suma2 += i
    contador2 +=1

promediode5=(suma2/contador2)

if promedio_de2 > promediode5:
  print("El promedio de los multiplos de 2 es mayor que el promedio de los multiplos de 5")
else:
  print("El promedio de los multiplos de 5 es mayor que el promedio de los multiplos de 2")



#17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5. 

suma = 0
contador = 0
numero = int(input("Ingrese un numero: "))

while numero != 0:
    if numero % 10 == 5:  
        suma += numero
        contador += 1
    numero = int(input("Ingrese un numero: "))  

if contador > 0:  
    promedio = suma / contador
    print("El promedio de los numeros terminados en 5 es:", promedio)
else:
    print("No se ingresaron numeros terminados en 5.")


#18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.

for i in range(10, 0, -1):
  print(i)

#19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.

numero= int(input("Ingrese un numero: "))
print("La tabla de", numero, "es:")
for i in range(1, 11):
  print(numero, "x",i, "=", numero*i)

20# Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.

n = int(input("Ingrese un número entero: "))
suma_factoriales = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    suma_factoriales += factorial
print(f"La sumatoria de las factoriales de los números entre 1 y {n} es: {suma_factoriales}")
  

'''#**Ejercicio 1**

#Crear un programa que imprima el mensaje "Hola mundo!" por pantalla

print ('"Hola Mundo!" ')


#**Ejercicio 2**

#Crear un programa que almacene el mensaje "Hola mundo!" en una variable y luego lo imprima por pantalla

a = ' "Hola mundo!" '
print (a)

#**Ejercicio 3**

#Crear un programa que le pida al usuario nombre y edad e imprima ambos datos en renglones distintos

nombre = input('Ingresá tu nombre: ')
edad = input ('Ingresá tu edad: ')
print ('El nombre ingresdo es'+' '+ nombre)
print ('La edad ingresada es'+' '+ edad)



#**Ejercicio 4**

#Crear un programa que pregunte el nombre de usuario y un número entero. Imprima por pantalla en líneas distintas el nombre de usuario tantas veces como el número introducido.

nombre = input('Ingresá tu nombre: ')
entero = int(input('Ingresá un número entero: '))
for entero in range(entero):
    print(nombre)

#**Ejercicio 4**

#Idem anterior, pero que también aparezcan las líneas numeradas.


nombre = input('Ingresá tu nombre: ')
entero = int(input('Ingresá un número entero: '))
for indice, _ in enumerate(range(1, entero + 1)):
    print(f"{indice + 1}. {nombre}")





#**Ejercicio 5**

#Idem anterior, pero que también aparezcan las líneas numeradas.


nombre = input('Ingresá tu nombre: ')
entero = int(input('Ingresá un número entero: '))
for i, _ in  enumerate(range(entero), start=1):
    print (f"{i}:{nombre})




#**Ejercicio 6**

#Crear un programa que pregunte el nombre de usuario y se muestre por pantalla: `*nombre* tiene *n* letras`



nombre = input('Ingresá tu nombre: ')
largo = len(nombre)
print(f"La longitud de la cadena es: {largo}")






#**Ejercicio 7**

#Crear un programa que realice la siguiente operación aritmética: `[ (3 + 2) / 2 * 5 ]^2`

operacion = ((3 + 2) / 2 * 5) ** 2
print(f"El resultado de la operación es: {operacion}")



#**Ejercicio 8**

#Crear un programa que pida al usuario dos números enteros *m* y *n* y muestre por pantalla lo siguiente:

#`m dividido por n da c, con resto r`

#siendo m y n los números ingresados por el usuario, c el cociente y r el resto de la división.


m = int(input('Ingresá un número entero: '))
n = int(input('Ingresá un número entero: '))
c = m//n
r = m%n

print(f"{m} dividido por {n} da {c}, con resto {r}")







**Ejercicio 9**

Crear un programa que pregunte al usuario una cantidad a invertir, 
el porcentaje de interés anual, y el número de años de inversión.
Muestre por pantalla el interés obtenido en la inversión. 
Fórmula de interés obtenido =   capital x interés x años


importe = int(input('Ingresar cantidad a Invertir: '))
porcentaje = int(input('Porcentaje de interés anual: '))
años = int(input('Años de inversión: '))
obtenido = ( importe * porcentaje * años)
print(f'Interes obtenido: {str(obtenido)}')





**Ejercicio 10**

Una fábrica de juguetes produce payasos y ositos. La empresa de logística cobra por el peso de cada entrega.
Sabiendo que cada payaso pesa 450 gr y cada osito 520g,
crear un programa que pida las unidades vendidas de cada artículo y 
devuelva por pantalla el peso total del pedido a despachar.'''



pp = 450
po = 520

cantidpp = int(input('Ingresá la cantidad de payasos comprados: '))
cantidpo = int(input('Ingresá la cantidad de ositos comprados: '))
 
pesototalpp = cantidpp * pp
pesototalpo = cantidpo * po

totalpedido = pesototalpp * pesototalpo
totalkilo = totalpedido /1000

print(f"El peso total del pedido a despachar: {totalkilo}")

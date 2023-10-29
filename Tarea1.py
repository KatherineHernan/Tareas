#Define una variable de cada tipo de primitivo
print('Calculadora de IMC')
entero_dos = float(input('Cuanto pesas? (Kilos) '))
entero_uno = float (input('Cuanto mides? (metros)'))
resultado = float( entero_dos / entero_uno)

print('El IMC es ' + str(resultado))
print('Igual y esta desactualizado  ')
cadena_de_texto = input('Tenes algun sue;o? Dimelo')
print('Veo en tu futuro que estas logrando' + cadena_de_texto)

#Los números se dividen en tres tipos de datos de Python:
#int / Integer: Int puede almacenar todos los valores enteros. 
#Este tipo de datopuede ser de cualquier tamaño. No hay límite de tamaño
#float: el flotante incluye todos los valores de punto flotante.
#Tampoco hay restricciones sobre el tamaño de un número de punto flotante.
#Fuente: https://eiposgrados.com/blog-python/tipos-de-datos-de-python/#:~:text=Los%20n%C3%BAmeros%20se%20dividen%20en,No%20hay%20l%C3%ADmite%20de%20tama%C3%B1o.

print('Calculo de la suma de numeros pares')

n= int(input('Ingrese el numero de terminos'))
s= 0
i=2
while (i <= 2*n):
    s= s + i
    i= i + 2 
    print('el valor de la suma de pares es', s)

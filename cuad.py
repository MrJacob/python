#!/usr/bin/env python
""" Un programa sencillo, para calcular cuadrados
de números """
 
def main():
    print ("Se calcularán cuadrados de números")
 
    n1 = input("Ingrese un número entero: ")
    n2 = input("Ingrese otro número entero: ")

    n4 = int(n1) #parse string into an integer
    n5 = int(n2) #parse string into an integer
 
    for x in range(n4, n5):
        y = x * x
        print("The result is:", y
              )
 
main()

"""PROGRAMA QUE DETERMINE EL NUMERO MAYOR"""


print("------------------------------")
print("--------NUMERO MAYOR----------")
print("------------------------------")


# input
X = int(input("Ingrese el valor de X: ")) 
Y = int(input("Ingrese el valor de Y: "))
Z = int(input("Ingrese el valor de Z: "))

# procesing 
if X > Y and X > Z :
    msj = X
else:
    Y > X and Y > Z 
    msj = Y
if Z > X and Z > Y:
    msj = Z


# output
print("El numero mayor es: " + str(msj))

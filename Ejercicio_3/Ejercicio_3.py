"""PROGRAMA QUE DETERMINE SI UN NUMERO ES ENTERO POSITIVO DE 4 DIGITOS"""


print("-----------------------------------------------------")
print("--------NUMERO ENTERO POSITIVO DE 4 DIGIROS----------")
print("-----------------------------------------------------")


# input
X = int(input("Ingrese el valor de X: "))

# procesing 
X
if X > 0 and X > 999 :
    msj = X
else:
    X < 0 and X > 999 
    msj = "Error"

# output
print("El numero es entero positivo de 4 digitos: " + str(msj))

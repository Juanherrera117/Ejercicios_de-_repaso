"""PROGRAMA QUE DETERMINE SI LA SUMA DE LOS DOS ULTIMOS DIGITOS 
ES UN NUMERO DE 1 DIGITO"""


from math import trunc


print("---------------------------------------------------------------------")
print("--------LA SUMA DE LOS DOS ULTIMOS ES UN NUMERO DE 1 DIGITO----------")
print("---------------------------------------------------------------------")


# input
X = int(input("Ingrese el valor de X: ")) 
Y = int
A = int
B = int
S = int

# procesing 
Y = X % 100
A = Y > 10
A = trunc(Y/10)   
B = Y % 10
S = (A + B)

if S <= 9:
    msj = S
else:
    S > 10
    msj = "Error"

# output
print("Los dos ultimos digitos de " + str(X) + " son: " + str(Y) + 
" Entonces " + str(A) + " mas " + str(B) + " Es " + str(msj))
"""PROGRAMA QUE RESUELVE LAS RAICES DE
UNA ECUACION DE SEGUNDO GRADO"""


print("---------------------------------------")
print("--------RAICES DE SEGUNDO GRADO--------")
print("---------------------------------------")

# input
A = int(input("Ingrese el valor de A:\n")) 
B = int(input("Ingrese el valor de B:\n"))
C = int(input("Ingrese el valor de C:\n"))

# procesing
disco = ((B**2)-(4*A*C))
R = (disco)**(0.5)

if (disco>0):
    X1 = ((-B)+R)/(2*A)
    X2 = ((-B)-R)/(2*A)
    print("X1= ",X1)
    print("X2= ",X2)
elif (disco==0):
    X1 = ((-B)+R)/(2*A)
    X2 = ((-B)-R)/(2*A)
    print("X1= ",X1)
    print("X2= ",X2)
else: 
    print("Solucion imaginaria")

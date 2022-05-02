"""PROGRAMA QUE DETERMINE EL VALOR A PAGA EN UNA LLAMADA"""

print("------------------------------")
print("--------VALOR A PAGAR---------")
print("------------------------------")

# input
X = int(input("Tiempo de la llamada: ")) 




# procesing 
if X == 3:
    msj = 300
else: 
    X > 3
    msj = 300 + int((X - 3) * 50)




# output
print("Total: " " $ " + str(msj))
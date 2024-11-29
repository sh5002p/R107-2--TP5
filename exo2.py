N1 = str(input("Donner la note de l élève : "))
C1 = N1.split(" ")
Note1 = float(C1[0])
coeff1 = float(C1[1])
print(Note1,coeff1)
N2 = str(input("Donner la deuxieme note de l élève : "))
C2 = N2.split(" ")
Note2 = float(C2[0])
coeff2 = float(C2[1])
print(Note2,coeff2)
noteglo = ((Note1 * coeff1)+(Note2 * coeff2))/2
if noteglo >= 10:
    print("L'élève est admis")
    print(noteglo)
else :
    print("L'élève n'est pas admis")
    print(noteglo)
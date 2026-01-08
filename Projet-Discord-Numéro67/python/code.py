from decimal import Decimal, getcontext

print("Enoncé: \nCalculate the 1000 digits of decimal of PI iteratively")
print("Méthode: Formule de Leibniz (π/4 = 1 - 1/3 + 1/5 - 1/7 + ...)")

# Définir la précision (plus que 1000 pour être sûr)
getcontext().prec = 1002

PI = Decimal(0)
iteration = 1000000  # Il faut beaucoup d'itérations pour une bonne précision

for i in range(iteration):
    term = Decimal(1) / Decimal(2 * i + 1)
    if i % 2 == 0:
        PI += term  # Termes positifs pour i pair (1, 1/5, 1/9...)
    else:
        PI -= term  # Termes négatifs pour i impair (1/3, 1/7, 1/11...)

result = PI * 4

print(f"π approximé avec {iteration} itérations :")
print(result)

print("\n \n \n \n")

print("Méthode 2: Algorithme de Chudvosky")

# précision
getcontext().prec = 105

def calcul_pi():
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, 100):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    return C / S

pi = calcul_pi()
print(pi)

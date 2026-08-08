import math

pX1, pY1 = input().split()
pX2, pY2 = input().split()
pX1, pY1 = float(pX1), float(pY1)
pX2, pY2 = float(pX2), float(pY2)

distancia  = math.sqrt(pow(pX2 - pX1, 2) + pow(pY2 - pY1, 2))

print(f"{distancia:.4f}")
from math import degrees, sqrt, asin, ceil

ab = int(input())
bc = int(input())

ac = sqrt(ab**2 + bc**2)

bac = degrees(asin(bc / ac))

if (float(bac) % 1) >= 0.5:
    bac = ceil(bac)
else:
    bac = round(bac)

print(str(180 - 90 - bac)+'°')

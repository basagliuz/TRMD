import math

def cylvol(radius, height):
    return height * (2 * math.pi * radius)

r = 5
h = 10
v = cylvol(r, h)
print("Il volume di un cilindro di raggio {} e altezza {} è {}." .format(r, h, v))
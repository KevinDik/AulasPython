import math

def are(r):
    return math.pi * (r ** 2)


print(are(2))
print(are(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for valor in raios:
    areas.append((are(valor)))
print(areas)

areas = map(are, raios)
print(list(areas))

print(list(map(lambda r: math.pi * (r ** 2), raios)))

cidades = [('berlin', 29), ('Cairo', 36), ('Buenos aires', 19), ('Los angeles', 26), ('Toquio', 27), ('Nova york', 28), ('Londres', 22)]
print(cidades)

# F = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], [9/5*dado[1]+32])
print(list(map(c_para_f, cidades)))

print(list(map(lambda dado: (dado[0], [9/5*dado[1]+32]), cidades)))

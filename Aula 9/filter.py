import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)
print(media)
res = filter(lambda x: x > media, dados)
print(list(res))
print(list(res))

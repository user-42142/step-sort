import matplotlib.pyplot as plt
import random
import bisect

# Embaralhar a lista inicial
a = list(range(100))
random.shuffle(a)

# Inicializar lista ordenada anterior como vazia
l1_anterior = []

while True:
    plt.figure()
    plt.bar(range(len(a)), a)
    plt.show()

    l1 = []
    l2 = []

    # Parte não ordenada: só os elementos da rodada atual
    parte_nao_ordenada = a[:len(a) - len(l1_anterior)]

    for i in parte_nao_ordenada:
        if not l1:
            l1.append(i)
            continue
        if i > l1[-1]:
            l1.append(i)
        else:
            l2.append(i)

    # Aplicar busca binária em l1_anterior se existir
    if l1_anterior:
        index = bisect.bisect_right(l1_anterior, l1[-1])
        l1.extend(l1_anterior[index:])
        l2.extend(l1_anterior[:index])

    a = l2 + l1
    l1_anterior = l1[:]

    if len(l1) == len(a):
        break


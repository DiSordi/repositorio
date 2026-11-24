a1,a2,a3=int(input("Insira o primeiro valor: ")),int(input("Insira o segundo valor: ")),int(input("Insira o terceiro valor: "))
lista=[a1,a2,a3]
lista.sort()
lista.pop(2)
lista.pop(0)
print(f'O número do meio é {lista}')
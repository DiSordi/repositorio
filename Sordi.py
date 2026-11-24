'''a1,a2,a3=int(input("Insira o primeiro valor: ")),int(input("Insira o segundo valor: ")),int(input("Insira o terceiro valor: "))
lista=[a1,a2,a3]
lista.sort()
lista.pop(2)
lista.pop(0)
print(f'O número do meio é {lista}')
print(f"A média é {(a1+a2+a3)/3}")'''
anterior=0
soma=0
listadenumeros=[]
while True:
    opção=int(input("O que você deseja fazer? \n (1) - Adicionar número \n (2) - Terminar sequência \n opção: "))
    if opção == 1:
        numero=int(input("Digite um número: "))
        
        if numero > 0 and numero > anterior:
                listadenumeros.append(numero)
                soma=soma+numero
                anterior=numero

        else: 
                print(f'Numero menor ou igual ao que o anterior digitado, sequência quebrada')
                print(f'A soma dos digitos digitados foi = {soma}')
                break
    elif opção == 2:
          print(f"Fim da sequência, a soma dos números foi: {soma} ")
          
          print("\n\nLá-lá-lá-lá-lá, Brizola\nLá-lá-lá-lá-lá, Brizola\nUm voto pro Brizola\nsó pode nos trazer\nUm tempo bem melhor pra se viver\nBrizola presidente\nsó pode nos trazer\nUm tempo bem melhor pra se viver\n\n")
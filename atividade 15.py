idade=int(input("Digite sua idade: "))
tem_convite=input("Tem convite? (s/n): ")
acompanhado=input("Está acompanhado? (s/n): ")

if idade>=18 and tem_convite=="s":
    print("Entrada permitida")

elif idade<18 and acompanhado=="s":
    print("Entrada permitida com responsável")

else:
    print("Entrada negada")
    
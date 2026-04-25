idade=int(input("Digite sua idade: "))
tem_ingresso=input("Possui ingresso? (s/n):")

if idade>=18 and tem_ingresso=="s":
    print("Entrada permitida")

else:
    print("Entrada negada")
    
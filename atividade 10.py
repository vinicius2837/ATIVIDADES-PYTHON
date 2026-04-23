idade=int(input("Digite sua idade: "))

if idade<18:
    print("Acesso negado à promoção")

else:
    cartao_fidelidade=input("Possui cartão fidelidade?(s/n): ")

    if cartao_fidelidade=="s":
        print("Desconto aplicado!")
    
    else:
        print("Cadastre-se para obter desconto")


    
    
idade=int(input("Digite a sua idade: "))
estudante=input("É estudante? (s/n): ")

if idade<18 or estudante=="s":
    print("Tem direito a meia entrada")

else:
    print("Entrada inteira")
    
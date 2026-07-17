estoque = 15
quantidade_solicitada = int(input("Digite a quantidade que você quer!:"))
if quantidade_solicitada > estoque:
    print("Estoque Insuficiente.")
elif estoque < 16:
    print("Pedido Aprovado.")
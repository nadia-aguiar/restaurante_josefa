cardapio_lista = {
    "HAMBURGER": 100,
    "HAMBURGER VEGETARIANO": 100,
    "CACHORRO-QUENTE": 50, "X-BURGER": 50,
    "EMPADA DE CARNE": 50,
    "EMPADA DE LEGUMES": 50,
    "RISOLES DE QUEIJO": 50,
    "ROLINHO PRIMAVERA": 50,
    "SUCO DE CAJÁ": 25,
    "SUCO DE ACEROLA": 25,
    "SPRITE": 25,
    "ÁGUA MINERAL SEM GÁS": 25,
    "ÁGUA MINERAL COM GÁS": 25,
    "BATATA FRITA": 25,
    "MOLHO EXTRA": 25
}

cardapio = {
    "HAMBURGER": 18,
    "HAMBURGER VEGETARIANO": 15,
    "CACHORRO-QUENTE": 10,
    "X-BURGER": 12,
    "EMPADA DE CARNE": 8,
    "EMPADA DE LEGUMES": 6,
    "RISOLES DE QUEIJO": 8,
    "ROLINHO PRIMAVERA": 10,
    "SUCO DE CAJÁ": 7,
    "SUCO DE ACEROLA": 8,
    "SPRITE": 5,
    "ÁGUA MINERAL SEM GÁS": 4,
    "ÁGUA MINERAL COM GÁS": 5,
    "BATATA FRITA": 10,
    "MOLHO EXTRA": 6
}


def pedir(nome):
    mostrar_cardapio(nome)

    lista_de_comidas = {}
    pedido = input(f"Gostaria de pedir algo {nome}? Sim ou Sair ").title()

    while pedido != "Sair":
        comida = input(f"Qual o pedido de hoje {nome}? ").upper()
        if comida in cardapio_lista:
            quantidade = int(input(f"Qual a quantidade de {comida}? "))
            if quantidade <= cardapio_lista.get(comida):
                # lista_de_comidas.append({quantidade: comida})
                lista_de_comidas[comida] = quantidade
            else:
                print("No momento não temos essa quantidade. ")
                mostrar_cardapio(nome)
        else:
            print("no momento não temos esse produto. ")
            mostrar_cardapio(nome)

        pedido = input(f"Gostaria de pedir algo {nome}? Sim ou Sair ").title()

    if pedido == "Sair":
        print(f"Seu pedido de hoje é: {lista_de_comidas}. ")

    return lista_de_comidas


def dados_cliente():
    nome_cliente = input(
        "Olá. Seja Benvinda na lanchonete da Josefa. Por favor digite seu nome: "
    )
    return nome_cliente


def mostrar_cardapio(nome):
    print(f"Confira nosso cardápio, {nome}")
    print(cardapio)


def pagamento(pedidos, nome):
    total = 0
    for chave in pedidos:
        valor_de_venda = cardapio.get(chave)
        quantidade_comprada = pedidos.get(chave)

        total = total + (valor_de_venda * quantidade_comprada)

    print(f"Olá, {nome}. O valor a ser pago é: {total} reais.")


if __name__ == '__main__':
    nome = dados_cliente()

    pedidos = pedir(nome)

    if pedidos:
        pagamento(pedidos, nome)


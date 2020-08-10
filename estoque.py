
def cardapio ():
    cardapio_lista = ["HAMBURGER", "HAMBURGER VEGETARIANO", "CACHORRO-QUENTE", "X-BURGER", "EMPADA DE CARNE",
                      "EMPADA DE LEGUMES", "RISOLES DE QUEIJO", "ROLINHO PRIMAVERA", "SUCO DE CAJÁ", "SUCO DE ACEROLA",
                      "SPRITE", "ÁGUA MINERAL SEM GÁS", "ÁGUA MINERAL COM GÁS", "BATATA FRITA", "MOLHO EXTRA"]
					  
    return cardapio_lista




def atualizar_estoque():
    produtos = cardapio()
    lista_atualizada = []
    
    for produto in produtos:
        quantidade_estoque = input (f"Qual a quantidade de {produto}? ")
        lista_atualizada.append({produto: quantidade_estoque})
    adicionar_produto = input("Gostaria de adicionar algo mais? sim ou não? ")
	
    while adicionar_produto == "sim":
        produto_estoque = input("Qual o novo produto no estoque? ")
        quantidade_estoque = input(f"Qual a quantidade de {produto_estoque}? ")
        lista_atualizada.append({produto_estoque: quantidade_estoque})
        adicionar_produto = input("Gostaria de adicionar algo mais? sim ou não? ")
		
    if adicionar_produto == "não":
        print (f"O estoque atual conta com {lista_atualizada}")
		
    return lista_atualizada



if __name__ == '__main__':

    atualizar_estoque()

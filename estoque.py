import json

#questao dois

def carregar_estoque():
    with open('questao-dois.json', 'r') as f:
        data = json.load(f)
    return data['estoque']

def encontrar_produto(estoque, codigo):
    for produto in estoque:
        if produto['codigoProduto'] == codigo:
            return produto
    return None

def main():
    estoque = carregar_estoque()
    movimentacoes = []
    proximo_id = 1
    
    while True:
        print("\n--- Controle de Estoque ---")
        print("1. Nova movimentação")
        print("2. Ver movimentações")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":

            print("\nProdutos:")
            for p in estoque:
                print(f"{p['codigoProduto']} - {p['descricaoProduto']} (Estoque: {p['estoque']})")
            
            codigo = int(input("\nCódigo do produto: "))
            produto = encontrar_produto(estoque, codigo)
            
            if not produto:
                print("Produto não encontrado!")
                continue
            
            print("Tipo de movimentação:")
            print("1 - Entrada")
            print("2 - Saída")
            tipo_num = input("Escolha (1 ou 2): ")
            
            if tipo_num == "1":
                tipo = "entrada"
            elif tipo_num == "2":
                tipo = "saida"
            else:
                print("Opção inválida!")
                continue
            
            quantidade = int(input("Quantidade: "))
            descricao = input("Descrição: ")
            
            if tipo == "entrada":
                produto['estoque'] += quantidade
            elif tipo == "saida":
                if produto['estoque'] >= quantidade:
                    produto['estoque'] -= quantidade
                else:
                    print("Estoque insuficiente!")
                    continue
            
            movimentacao = {
                'id': proximo_id,
                'produto': produto['descricaoProduto'],
                'tipo': tipo,
                'quantidade': quantidade,
                'descricao': descricao
            }
            
            movimentacoes.append(movimentacao)
            proximo_id += 1
            
            print(f"\nMovimentação #{movimentacao['id']} registrada!")
            print(f"Estoque atual de {produto['descricaoProduto']}: {produto['estoque']}")
        
        elif opcao == "2":
            if not movimentacoes:
                print("Nenhuma movimentação registrada.")
            else:
                print("\nMovimentações:")
                for mov in movimentacoes:
                    print(f"#{mov['id']} - Produto: {mov['produto']} - Tipo: {mov['tipo']} - Quantidade: {mov['quantidade']} - Descrição: {mov['descricao']}")
        
        elif opcao == "3":
            print("Finalizando sessão!")
            break

if __name__ == "__main__":
    main()

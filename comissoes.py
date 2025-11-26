import json

# questao um

def calcular_comissao(valor):
    if valor < 100:
        return 0
    elif valor < 500:
        return valor*0.01
    else:
        return valor*0.05

def main():
    with open('questao-um.json', 'r') as f:
        data = json.load(f)
    
    comissoes = {}
    
    for venda in data['vendas']:
        vendedor = venda['vendedor']
        valor = venda['valor']
        
        if vendedor not in comissoes:
            comissoes[vendedor] = 0
        
        comissoes[vendedor] += calcular_comissao(valor)
    
    print("Comissões por vendedor:")
    
    total = 0
    for vendedor, comissao in comissoes.items():
        print(f"{vendedor}: R$ {comissao:.2f}")
        total += comissao
    
    print(f"Total: R$ {total:.2f}")

if __name__ == "__main__":
    main()
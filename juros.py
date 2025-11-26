from datetime import datetime

# questao tres

def calcular_juros():
    print("--- Calculadora de Juros por Atraso ---")
    
    valor = float(input("Valor original: R$ "))
    data_vencimento = input("Data de vencimento (DD/MM/AAAA): ")
    
    vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
    hoje = datetime.now()
    
    dias_atraso = (hoje-vencimento).days
    
    if dias_atraso <= 0:
        print("Sem atraso. Valor permanece o mesmo.")
        print(f"Valor total: R$ {valor:.2f}")
    else:
        taxa_juros = 0.025  
        juros = valor*taxa_juros*dias_atraso
        valor_total = valor+juros
        
        print(f"Dias de atraso: {dias_atraso}")
        print(f"Valor original: R$ {valor:.2f}")
        print(f"Juros ({taxa_juros*100}% ao dia): R$ {juros:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")

if __name__ == "__main__":
    calcular_juros()

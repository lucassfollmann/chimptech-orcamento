class Orcamento:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.lista_servico = []
        self.lista_valor = []

    def adicionar_servico(self, item, valor_item):
        self.lista_servico.append(item)
        self.lista_valor.append(valor_item)
    
    def calcular_total(self, percentual_desconto=0.10):
        valor_total = sum(self.lista_valor)
        if valor_total > 500:
            desconto = valor_total * percentual_desconto
        else:
            desconto = 0
        valor_final = valor_total - desconto
        return valor_total, desconto, valor_final
    
    def salvar_arquivo(self, valor_total, desconto, valor_final):
   
        orcamento_texto = f"== ORÇAMENTO - ChimpTech ===\n"
        orcamento_texto += f"Cliente: {self.nome_cliente}\n\n"
        orcamento_texto += "Serviços:\n"

        for i in range(len(self.lista_servico)):
            orcamento_texto += f"- {self.lista_servico[i]}: R$ {self.lista_valor[i]:.2f}\n"
        
    
        orcamento_texto += f"\nValor original: R$ {valor_total:.2f}\n"
        orcamento_texto += f"Desconto: R$ {desconto: .2f}\n"
        orcamento_texto += f"Valor Final: R$ {valor_final: .2f}\n"
        orcamento_texto += "=================================="
            
        nome_arquivo = f"orcamento_{self.nome_cliente}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(orcamento_texto)
            
        print(f"\nOrçamento salvo em: {nome_arquivo}")
    
continuar_orcamento = "s"
while continuar_orcamento == "s":
    nome = input("Nome do cliente: ")
    orcamento = Orcamento(nome)
    
    continuar_servico = "s"
    while continuar_servico == "s":
        item = input("Outros serviços prestados: ")
        valor_item = float(input("Valor do serviço (R$): "))
        orcamento.adicionar_servico(item, valor_item)
        continuar_servico = input("Deseja adicionar outro serviço? (s/n): ")
        
    percentual = float(input("Percentual de desconto (ex: 10 para 10%, 0 para nenhum): ")) / 100
    valor_total, desconto, valor_final = orcamento.calcular_total(percentual)
    
    print(f"\nLista de Serviços:")
    for servico in orcamento.lista_servico:
        print(f"- {servico}")
    print(f"Valor original: R$ {valor_total: .2f}")
    print(f"Desconto: R% {desconto: .2f}")
    print(f"Valor Final: R$ {valor_final: .2f}")
    
    orcamento.salvar_arquivo(valor_total, desconto, valor_final)
    
    continuar_orcamento = input("\nDeseja gerar outro orçamento (outro cliente)? (s/n): ")
    
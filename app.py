import streamlit as st

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

    def gerar_texto(self, valor_total, desconto, valor_final):
        texto = f"=== ORÇAMENTO - ChimpTech ===\n"
        texto += f"Cliente: {self.nome_cliente}\n\n"
        texto += "Serviços:\n"
        for i in range(len(self.lista_servico)):
            texto += f"- {self.lista_servico[i]} R$ {self.lista_valor[i]:.2f}\n"
        texto += f"\nValor original: R$ {valor_total:.2f}\n"
        texto += f"Desconto: R$ {desconto:.2f}\n"
        texto += f"Valor Final: R$ {valor_final:.2f}\n"
        return texto
                             
if "orcamento" not in st.session_state:
    st.session_state.orcamento = None

nome_cliente = st.text_input("Nome do cliente")

if nome_cliente and st.session_state.orcamento is None:
    st.session_state.orcamento = Orcamento(nome_cliente)

st.subheader("Adicionar Serviço")
item = st.text_input("Serviço prestado")
valor_item = st.number_input("Valor do serviço (R$)", min_value=0.0, step=10.0)

if st.button("Adicionar Serviço"):
    st.session_state.orcamento.adicionar_servico(item, valor_item)

if st.session_state.orcamento and st.session_state.orcamento.lista_servico:
    st.subheader("Serviços adicionado")
    for i in range(len(st.session_state.orcamento.lista_servico)):
        st.write(f"-{st.session_state.orcamento.lista_servico[i]}: R$ {st.session_state.orcamento.lista_valor[i]:.2f}")


    percentual = st.slider("Percentual de desconto(%)", 0, 50, 0)
    if st.button("Gerar Orçamento"):
        valor_total, desconto, valor_final = st.session_state.orcamento.calcular_total(percentual / 100)

        st.write(f"Valor original: R$ {valor_total:.2f}")
        st.write(f"Desconto: R$ {desconto:.2f}")
        st.write(f"Valor Final: R$ {valor_final:.2f}")

        texto_orcamento = f"=== Orçamento - ChimpTech ===\n"
        texto_orcamento = st.session_state.orcamento.gerar_texto(valor_total, desconto, valor_final)

        st.download_button(
            label="Baixar Orçamento (.txt)",
            data=texto_orcamento,
            file_name=f"orcamento_{nome_cliente}.txt",
            mime="text/plain"
        )
    st.divider()
    if st.button("Novo orçamento (outro cliente)"):
        st.session_state.orcamento = None
        st.rerun




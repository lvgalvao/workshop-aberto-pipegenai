# frontend.py

import streamlit as st
from datetime import datetime, time

# Função principal para o frontend
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")

    # Campos de entrada para os dados
    email = st.text_input("Email do Vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    # Botão de submissão
    if st.button("Salvar"):
        # Combinando a data e hora selecionadas para criar o datetime
        data_hora = datetime.combine(data, hora)

        # Exibindo os dados na tela
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")

if __name__ == "__main__":
    main()

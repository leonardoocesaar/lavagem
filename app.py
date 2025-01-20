import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'registro-lavagem.csv'
registro_lavagem = pd.read_csv(file_path, delimiter=';', engine='python')

# Configurar título e subtítulo
st.title("Lavagem de isoladores ARGO I") 
st.divider()
st.subheader("Escolha a subestação")

# Lista de subestações disponíveis
subestacoes = ["bacabeira", "Tianguá II", "Acaraú III", "Parnaíba III", "Pecém II"]
escolha_se = st.multiselect("ARGO I - SE", subestacoes)

# Verificar se alguma subestação foi selecionada
if escolha_se:
    # Filtrar os dados pelas subestações selecionadas
    dados_filtrados = registro_lavagem[registro_lavagem['Qual SE foi realizada a Lavagem em LV?\xa0'].isin(escolha_se)]

    # Exibir o número de lavagens realizadas por subestação
    st.subheader("Resumo das Lavagens")
    lavagens_por_se = dados_filtrados['Qual SE foi realizada a Lavagem em LV?\xa0'].value_counts()
    for se, quantidade in lavagens_por_se.items():
        st.write(f"Subestação {se}: {quantidade} lavagem(ns)")

    # Exibir outros detalhes, se necessário
    st.subheader("Detalhes das Lavagens")
    st.dataframe(dados_filtrados)
else:
    st.write("Selecione uma ou mais subestações para visualizar os dados.")

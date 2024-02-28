from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(layout='wide')

st.title('Meu Dashboard 🤩')

st.sidebar.title('Configuração')

summary_file = Path.cwd() / "data" / "processed" / f"summary_recursos_disponiveis.pkl"

df = pd.read_pickle(summary_file)


def formatar_moeda(valor):
    return f'$ {valor:,.2f}'


df['Valor Formatado'] = df['Valor'].apply(formatar_moeda)

anos = st.multiselect('Selecione o ano', df['Ano'].unique())

dados = df[df['Ano'].isin(anos)]

if dados.empty:    
    st.markdown('Não há dados a serem exibidos!')
else:
    st.dataframe(dados, hide_index=True, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(dados, values='Valor', names='Objetivo', 
                    title=f'Distribuição de Recursos para os ODS - {dados["Ano"].unique()}',
                    color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.pie(df, values='Valor', names='Ano', 
                    title=f'Distribuição de Recursos para os ODS - {df["Ano"].unique()}',
                    color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)

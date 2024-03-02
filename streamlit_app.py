import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as ps


st.set_page_config(layout='centered', page_title='Open Data Day 2024', page_icon=':sunglasses:')

st.title('Open Data Day :sunglasses:')
st.subheader('Meu Dashboard')

summary_file = Path.cwd() / "data" / "processed" / f"summary_recursos_disponiveis.csv"

df = pd.read_csv(summary_file, dtype={'Ano': str})

ano_selecionado = st.selectbox('Selecione o ano:', df['Ano'].unique(), index=1)

dados = df[df['Ano'].isin([ano_selecionado])]

with st.expander(f'Recursos Disponíveis para o ODS {ano_selecionado}'):
    st.dataframe(dados, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f'Valor Total Disponível: $ {dados['Valor'].sum():,.2f}')
with col2:
    st.markdown(f'Percentual Total: %{dados['Percentual'].sum():.2f}')

fig = ps.pie(dados, 
             names='Objetivo', 
             values='Valor', 
             title=f'Recursos Disponíveis para os ODS - {ano_selecionado}')

st.plotly_chart(fig)

fig = ps.pie(dados, 
             names='Objetivo', 
             values='Valor', 
             title=f'Recursos Disponíveis para os ODS - {ano_selecionado}',
             color_discrete_sequence=ps.colors.sequential.Oranges)

st.plotly_chart(fig)
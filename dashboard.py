import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.title("Evolução e Importância da Programação")

# Texto introdutório
st.markdown("""
A programação evoluiu desde os algoritmos de Ada Lovelace até as linguagens modernas como Python.
Este dashboard apresenta a popularidade das linguagens de programação ao longo do tempo.
""")

dados = {
    'Ano': list(range(2010, 2026)),
    'Python': [5, 6, 7, 8, 10, 12, 15, 18, 22, 27, 33, 40, 48, 57, 67, 78],
    'Java': [20, 22, 24, 26, 28, 30, 32, 33, 34, 34, 33, 32, 30, 28, 25, 22],
    'C++': [15, 16, 17, 18, 19, 20, 21, 21, 20, 19, 18, 17, 16, 15, 14, 13]
}

df = pd.DataFrame(dados)

# Seleção de linguagens
linguagens = ['Python', 'Java', 'C++']
linguagem_selecionada = st.selectbox("Selecione a linguagem de programação:", linguagens)

# Gráfico de linha
fig = px.line(df, x='Ano', y=linguagem_selecionada, title=f'Popularidade do {linguagem_selecionada} ao longo do tempo')
st.plotly_chart(fig)

# Texto sobre a importância futura
st.markdown("""
### Importância da Programação no Futuro

A programação é fundamental para o desenvolvimento de tecnologias emergentes como inteligência artificial, automação e análise de dados. Aprender a programar capacita indivíduos a resolver problemas complexos e a contribuir para inovações que impactam positivamente a sociedade.
""")

import streamlit as st
import pandas as pd
import plotly.express as px

# Criando os dados para o dashboard
data = {
    "Elemento Avaliado": [
        "Personalidade e Genética",
        "Inteligências Individuais",
        "Saúde Emocional e Produtividade",
        "Neurocognição (Sensorial Moove)",
        "Gestão de Qualidade de Vida"
    ],
    "Pontuação Atingida": [750, 800, 780, 765, 700],
    "Pontuação Ideal": [850, 880, 850, 830, 800]
}

df = pd.DataFrame(data)

def dashboard():
    st.title("Análise NeuroAccess – Thiago Pereira")
    st.subheader("📌 Diretor de Franquia da SmartFit")

    # Score Geral
    st.metric(label="Pontuação Geral", value="765 / 1000", delta="-71 do ideal")

    # Gráfico de Barras Comparativo
    fig = px.bar(df, x="Elemento Avaliado", y=["Pontuação Atingida", "Pontuação Ideal"],
                 barmode="group", title="Comparação de Pontuações por Dimensão")
    st.plotly_chart(fig)

    # Gráfico Radar
    fig_radar = px.line_polar(df, r="Pontuação Atingida", theta="Elemento Avaliado",
                              line_close=True, title="Distribuição das Pontuações")
    st.plotly_chart(fig_radar)

    # Recomendações
    st.subheader("🔍 Análises e Recomendações")
    st.write("📌 **Personalidade e Genética:** Thiago tem alta disciplina, mas precisa melhorar flexibilidade cognitiva.")
    st.write("📌 **Inteligências Individuais:** Ótima análise lógica, mas pode aprimorar a comunicação interpessoal.")
    st.write("📌 **Saúde Emocional:** Boa regulação emocional, mas evitar sobrecarga.")
    st.write("📌 **Neurocognição:** Tempo de reação pode ser otimizado para decisões rápidas.")
    st.write("📌 **Gestão de Qualidade de Vida:** Melhorar descanso e recuperação para performance sustentável.")

    # Sugestões de Treinamentos
    st.subheader("🎯 Sugestões de Treinamentos")
    st.write("✅ **Liderança Estratégica e Gestão de Mudança** – Inova & Educa")
    st.write("✅ **Comunicação Assertiva e Gestão de Relacionamentos** – Inova & Educa")
    st.write("✅ **Gestão do Estresse e Performance** – Inova & Educa")
    st.write("✅ **Sensorial Moove – Desenvolvimento Cognitivo**")

if __name__ == "__main__":
    dashboard()

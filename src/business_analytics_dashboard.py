#!/usr/bin/env python3
"""
Business Analytics Dashboard - Wharton Capstone Project
Comprehensive Business Intelligence Platform
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# Funções utilitárias
def load_csv(file_path):
    """Carrega CSV, se existir. Retorna dataframe vazio se não existir."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        st.warning(f"Arquivo não encontrado: {file_path}")
        return pd.DataFrame()

# Dashboard principal
def main():
    st.set_page_config(page_title="Business Analytics Dashboard", page_icon="📊", layout="wide")
    st.title("📊 Business Analytics Dashboard")
    st.markdown("*Wharton Business Analytics Capstone Project*")
    st.sidebar.markdown("## Navegação")
    module = st.sidebar.selectbox("Selecione o módulo", [
        "Visão Geral",
        "Customer Analytics",
        "Operations Analytics",
        "People Analytics",
        "Financial Analytics"
    ])
    
    if module == "Visão Geral":
        show_overview()
    elif module == "Customer Analytics":
        show_customer_analytics()
    elif module == "Operations Analytics":
        show_operations_analytics()
    elif module == "People Analytics":
        show_people_analytics()
    elif module == "Financial Analytics":
        show_financial_analytics()

def show_overview():
    st.subheader("🔎 Visão Geral do Projeto")
    st.info("Este dashboard integra clientes, operações, RH e finanças. Use os módulos ao lado para análise detalhada.")

def show_customer_analytics():
    st.header("👥 Customer Analytics")
    df = load_csv("../data/customer_data.csv")
    if df.empty:
        st.error("Dados de clientes não encontrados.")
        return
    st.write(df.head())
    st.markdown("**Gráfico de segmentos:**")
    if 'segment' in df.columns:
        fig = px.histogram(df, x='segment', color='segment', title="Distribuição de Segmentos")
        st.plotly_chart(fig)
    # Exibir RFM, churn, etc.

def show_operations_analytics():
    st.header("🏭 Operations Analytics")
    df = load_csv("../data/operations_data.csv")
    if df.empty:
        st.error("Dados operacionais não encontrados.")
        return
    st.write(df.head())
    if 'supplier' in df.columns:
        fig = px.bar(df, x='supplier', y='on_time_rate', title="Pontualidade de Entrega por Fornecedor")
        st.plotly_chart(fig)
    # Mostrar scores, alocação, etc.

def show_people_analytics():
    st.header("👤 People Analytics")
    df = load_csv("../data/people_data.csv")
    if df.empty:
        st.error("Dados de RH não encontrados.")
        return
    st.write(df.head())
    if 'department' in df.columns:
        fig = px.bar(df, x='department', y='salary', title="Salário por Departamento")
        st.plotly_chart(fig)
    # Exibir indicadores de turnover, tenure, etc.

def show_financial_analytics():
    st.header("💰 Financial Analytics")
    df = load_csv("../data/financial_data.csv")
    if df.empty:
        st.error("Dados financeiros não encontrados.")
        return
    st.write(df.head())
    if {'date', 'revenue', 'cogs'}.issubset(df.columns):
        fig = px.line(df, x='date', y=['revenue', 'cogs'], title="Receita e Custo ao Longo do Tempo")
        st.plotly_chart(fig)
    # Mostrar margens, fluxo de caixa, etc.

if __name__ == "__main__":
    main()


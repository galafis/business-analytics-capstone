# Technical Documentation

## Business Analytics Capstone - Technical Guide

### Sumário

1. [Arquitetura do Projeto](#arquitetura)
2. [Estrutura de Dados](#estrutura-dados)
3. [Notebooks de Análise](#notebooks)
4. [Dependências](#dependencias)
5. [Instalação e Setup](#instalacao)

## Arquitetura do Projeto {#arquitetura}

Este projeto segue uma arquitetura modular para análise de dados de negócios, separando claramente:

- **data/**: Dados de entrada em formato CSV
- **notebooks/**: Jupyter notebooks para análises específicas
- **src/**: Código fonte reutilizável
- **docs/**: Documentação técnica e do usuário
- **tests/**: Testes automatizados

## Estrutura de Dados {#estrutura-dados}

### Arquivos de Dados

- `customer_data.csv`: Dados de clientes
- `operations_data.csv`: Dados operacionais
- `people_data.csv`: Dados de recursos humanos
- `financial_data.csv`: Dados financeiros

## Notebooks de Análise {#notebooks}

Cada notebook é especializado em um domínio específico:

1. `customer_analytics.ipynb`: Análise de clientes
2. `operations_analytics.ipynb`: Análise operacional
3. `people_analytics.ipynb`: Análise de pessoas/RH
4. `financial_analytics.ipynb`: Análise financeira

## Dependências {#dependencias}

Ver arquivo `requirements.txt` para lista completa de dependências.

## Instalação e Setup {#instalacao}

```bash
# Clone o repositório
git clone <repository-url>

# Instale as dependências
pip install -r requirements.txt

# Inicie Jupyter
jupyter notebook
```

## Contribuição

Para contribuir com este projeto, consulte o guia do usuário em `user_guide.md`.

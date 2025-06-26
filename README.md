# BookRecommendationTool - Motor de Recomendação de Livros

Este projeto foi desenvolvido no âmbito da Unidade Curricular de **Programação e Algoritmos em Ciências**, e consiste num sistema simples de **recomendação de livros**, implementado em **Python**, com base em técnicas de **Processamento de Linguagem Natural (NLP)** e **cálculo de similaridade**.

## Descrição do Sistema

O sistema recomenda livros a partir da combinação de:
- **Preferências de géneros literários** escolhidas pelo utilizador;
- **Tópicos extraídos automaticamente** das descrições e avaliações dos livros;
- **Matriz de similaridades** construída com base nas descrições e classificações de livros.

O utilizador pode selecionar géneros e tópicos do seu interesse, ou indicar livros previamente lidos e avaliados, e o sistema irá sugerir obras semelhantes com base nessas preferências.

## Dataset

Foi utilizado o dataset **Amazon Book Reviews**, disponível em [Kaggle](https://www.kaggle.com/datasets/), que contém dados extraídos da plataforma **Goodreads**:
- Títulos, categorias e descrições dos livros;
- Avaliações numéricas e comentários escritos;
- Dois ficheiros relacionados pela coluna `Title`.

## Dependências

Para instalar o ambiente com todas as bibliotecas necessárias, recomenda-se o uso de Conda:
```bash
conda env create -f requirements/environment.yml
conda activate recomendador-livros
```
## Passos para executar o programa
- Executar todos os notebooks, pela ordem assinalada;
- Correr o programa principal
```bash
  python programa_livros.py
```

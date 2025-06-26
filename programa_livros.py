# Importar módulos necessários

import pandas as pd
import numpy as np
import datetime
import time
import random
import os
from rapidfuzz.process import extractOne

# Função para corrigir a string do input (aproximar do título mais próximo)
def corrigir_string(user_input, choices):
    fuzz_input = extractOne(query=user_input, choices=choices, score_cutoff=75)
    return fuzz_input[0]



# Função para buscar livros semelhantes e salvá-los
def buscar_livros_semelhantes(df):
    input_book = str(input("Insira o nome do livro: "))
    
    input_book_com_correcao = corrigir_string(input_book, choices=df["Title"])
    print("Apresentando recomendações para o livro {}\n".format(input_book_com_correcao))

    recommendations = pd.DataFrame(df.nlargest(11,input_book_com_correcao)['Title'])
    recommendations = recommendations[recommendations['Title']!=input_book_com_correcao]

    recommendations_list = recommendations.values.tolist()

    recomendacoes_salvas = []

    for index, recomendacao in enumerate(recommendations_list):
        print("Opções para a recomendação {}:".format(recomendacao))
        time.sleep(0.5)

        choice = int(input("\n 1 - Adicionar livro à lista de livros salvos \n \
                            2 - Pular livro \n \
                            3 - Fechar lista de recomendações para o livro\n \
                            >>> "))

        if choice == 1:
            recomendacoes_salvas.append(recomendacao)
            if index == len(recommendations_list) - 1:
                    print("Fim da lista de recomendações.")
                    return recomendacoes_salvas
        elif choice == 2:
            print(f"'{recomendacao}' foi pulado. \n")
            if index == len(recommendations_list) - 1:
                    print("Fim da lista de recomendações.")
                    return recomendacoes_salvas
        elif choice == 3:
            return recomendacoes_salvas
        

    return(recommendations_list)

    

# Função para visualizar os livros salvos
def visualizar_livros_salvos(lista_livros):
    print("\nLista de livros salvos até ao momento:\n")
    for i in lista_livros:
        print("{}".format(str(i[0])))
        
        
# Função para imprimir os livros salvos
def imprimir_livros_salvos(lista_livros):
    curdir = os.getcwd()
    data_horario_atual = datetime.datetime.now()
    data_horario_str = data_horario_atual.strftime("%Y%m%d_%H_%M_%S")
    
    ficheiro_final = "{}\listas_salvas\{}.txt".format(curdir, data_horario_str)

    with open(ficheiro_final, "w") as file:
        for i in lista_livros:
            file.write("{}\n".format(str(i[0])))



# Função para recomendar um livro aleatório
def random_book(df, lista_livros):
    # Obter os títulos dos livros
    titulos = df.columns.tolist()

    # Selecionar um título aleatório
    titulo_aleatorio = random.choice(titulos)

    lista_temp = []
    lista_temp.append(titulo_aleatorio)

    print(f"\nRecomendação: {titulo_aleatorio}")
    time.sleep(0.5)

    # Oferecer opções ao usuário
    while True:
        try:
            choice = int(input("\nO que deseja fazer? \n"
                               "1 - Adicionar livro à lista de livros salvos \n"
                               "2 - Descartar livro \n"
                               ">>> "))
            if choice == 1:
                if titulo_aleatorio not in lista_livros:
                    lista_livros.append(lista_temp)
                    print(f"'{titulo_aleatorio}' foi adicionado à sua lista de livros salvos.")
                else:
                    print(f"'{titulo_aleatorio}' já está na lista de livros salvos.")
                break
            elif choice == 2:
                print(f"'{titulo_aleatorio}' foi descartado.")
                break
            else:
                print("Opção inválida. Por favor, escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Por favor, insira 1 ou 2.")

    return lista_livros



# Função para alterar o gênero literário
def alterar_genero_literario():

    curdir = os.getcwd()
    
    try:
        choice = int(input("Escolha o gênero literário: \n \
                           1 - Ficção \n \
                           2 - Artes e cultura \n \
                           3 - Hobbies e Lazer \n \
                           4 - Crianças e Educação \n \
                           5 - Literatura e Poesia \n \
                           6 - Banda Desenhada \n \
                           0 - Cancelar\n \
                           >>> "))
        
    except:
        print("Erro!")
    
    while True:
        try:
            if choice == 1:
                print("Alterando a base de dados... Por favor, aguarde...")
                time.sleep(0.5)
                df = pd.read_csv(r"{}\databases\df_livros_fiction.csv".format(curdir))
                print("Base de dados alterada com sucesso!")
                time.sleep(0.5)
                return df
            elif choice == 2:
                print("Alterando a base de dados... Por favor, aguarde...")
                time.sleep(0.5)
                df = pd.read_csv(r"{}\databases\df_livros_arts.csv".format(curdir))
                print("Base de dados alterada com sucesso!")
                time.sleep(0.5)
                return df
            elif choice == 3:
                print("Alterando a base de dados... Por favor, aguarde...")
                time.sleep(0.5)
                df = pd.read_csv(r"{}\databases\df_livros_hobbies.csv".format(curdir))
                print("Base de dados alterada com sucesso!")
                time.sleep(0.5)
                return df
            elif choice == 4:
                print("Alterando a base de dados... Por favor, aguarde...")
                time.sleep(0.5)
                df = pd.read_csv(r"{}\databases\df_livros_kids.csv".format(curdir))
                print("Base de dados alterada com sucesso!")
                time.sleep(0.5)
                return df
            elif choice == 5:
                print("Alterando a base de dados... Por favor, aguarde...")
                time.sleep(0.5)
                df = pd.read_csv(r"{}\databases\df_livros_poetry.csv".format(curdir))
                print("Base de dados alterada com sucesso!")
                time.sleep(0.5)
                return df
            elif choice == 6:
                print("Alterando a base de dados... Por favor, aguarde...")
                time.sleep(0.5)
                df = pd.read_csv(r"{}\databases\df_livros_bd.csv".format(curdir))
                print("Base de dados alterada com sucesso!")
                time.sleep(0.5)
                return df
            elif choice == 0:
                print("Nenhuma alteração à base de dados foi feita")
                time.sleep(0.5)
                break
        except:
            print("Por favor, insira um input válido!")
            return
            
            
            
# Função main
def main():

    livros_salvos = []

    print("Bem-vindo ao programa de recomendação de livros para leitura")
    
    # Garantir que o DataFrame seja carregado antes de continuar
    while True:
        print("A carregar a base de dados... Por favor, aguarde")
        try:
            curdir = os.getcwd()
            df_livros = pd.read_csv(rf"{curdir}\databases\df_livros_bd.csv")
            print("Base de dados carregada com sucesso!")
            time.sleep(1)
            break
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado. Verifique o caminho e tente novamente.")
            time.sleep(2)
            return
        except Exception as e:
            print(f"Erro ao carregar o DataFrame: {e}")
            time.sleep(2)
            return

    while True:
        
        try:
            opcao = int(input("Insira a sua opção: \n \
                              1 - Buscar livros semelhantes \n \
                              2 - Visualizar lista de livros salvos \n \
                              3 - Imprimir lista de livros salvos \n \
                              4 - Receber recomendação aleatória \n \
                              5 - Alterar gênero literário \n \
                              0 - Encerrar programa \n \
                              >>> "
            ))

            if opcao == 0:
                print("Obrigado pela utilização. Até à próxima!")
                break
            elif opcao == 1:
                recomendacoes = buscar_livros_semelhantes(df = df_livros)
                if recomendacoes:
                    livros_salvos.extend(recomendacoes)
                    time.sleep(1)
            elif opcao == 2:
                visualizar_livros_salvos(livros_salvos)
                time.sleep(0.5)
            elif opcao == 3:
                try:
                    imprimir_livros_salvos(livros_salvos)
                    time.sleep(0.5)
                    print("Lista impressa com sucesso!")
                    time.sleep(0.5)
                except:
                    print("Falha na impressão da lista")
            elif opcao == 4:
                recomendacao = random_book(df_livros, lista_livros=livros_salvos)
                livros_salvos = recomendacao
                time.sleep(0.5)
            elif opcao == 5:
                df_livros = alterar_genero_literario()
            else:
                print("Opção inexistente! Insira uma opção válida")
    
        except:
            print("Insira uma opção válida")
            time.sleep(0.5)
            
            

# Chamar a main()
main()

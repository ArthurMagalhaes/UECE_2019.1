# -*- coding: utf-8 -*-
import pandas as pd
import random


database = pd.read_csv('data\\movies.csv') # Importa base de dados
database['nota'] = 0


def fill(user, data, rand=True):
    # user: string que contém o nome de um dos usuários do sistema
    # data: dataframe que contém os dados dos filmes mais as notas atribuídas pelo usuário, definidas de a 10, sendo 0 para filmes não assistidos
    # rand: define se as notas serão atribuídas pelo usuário ou serão geradas aleatoriamente (para teste)
    # return: um dicionário cujo valor é o dataframe com as notas atualizadas

    x = len(data)
    if rand:
        for i in range(x):
            r = random.random()
            if r < 0.4:
                data['nota'].iloc[i] = 0
            else:
                data['nota'].iloc[i] = round(11 * random.random())
            if data['nota'] == 11:
                data['nota'] = 10

        return {user: data}
    else:
        for i in range(x):
            print('Bem vindo, {}!'.format(data['nome']))
            database['nota'].iloc[i] = int(input('Digite uma nota (inteira de 1 a 10) de acordo com o quanto você '
                                                 'gostou do filme. Caso não tenha assistido, digite 0.\n'
                                                 + database.iloc[i]['titulo'] + ': '))
            print() # Quebra de linha


from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer, SigmoidLayer


def recomendation(data):
    # data: dataframe contendo as notas dos filmes assistidos pelo usuário
    # return: o objeto rede que contém as informações sobre o treinamento, e a lista recomendacoes com os titulos que podem interessar ao usuário

    rede = buildNetwork(8, 4, 2, 1, outclass=SoftmaxLayer, hiddenclass=SigmoidLayer, bias=True)
    base = SupervisedDataSet(8, 1)

    for row in data[data['nota'] > 0][['drama', 'acao', 'suspense', 'scifi',
                                       'terror', 'romance', 'comedia', 'fantasia', 'nota']].to_records():
        # Iteração que popula o objeto base

        values = tuple(row[['drama', 'acao', 'suspense', 'scifi', 'terror', 'romance', 'comedia', 'fantasia']])
        grade = (row['nota'] / 10,)

        base.addSample(values, grade)

    treinamento = BackpropTrainer(rede, dataset=base, learningrate=0.01, momentum=0.06)
    for i in range(100):  # Treinamento realizado em 100 épocas
        treinamento.train()
    erro = treinamento.train()

    recomendacoes = []
    for row in data[data['nota'] == 0].to_records():
        generos = []
        for g in list(zip(row[['drama', 'acao', 'suspense', 'scifi', 'terror', 'romance', 'comedia', 'fantasia']])):
            generos.append(g[0])

        if rede.activate(generos) >= (0.4 - erro / 2):  # Se a nota estimada for maior ou igual a 4 (com um desvio
            # igual a metade do erro máximo possível), então ela entra na lista de recomendações
            recomendacoes.append(row['titulo'])

    return rede, recomendacoes


data_test = fill('Gustavo', database, rand=True) # Faça 'rand=False' caso queira setar manualmente

r1, r2 = recomendation(data_test['Gustavo'])

print('Com base em seu histórico, achamos que estes filmes podem lhe interessar: ', end='\n\n')
for r in r2:
    print(r)

print('\nEsperamos ter sido útil!')

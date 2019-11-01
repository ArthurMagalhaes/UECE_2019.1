# -*- coding: utf-8 -*-
import pandas as pd

# Criação de uma base de dados (Filmes) para geração do sistema de recomendação.
data = []

data.append({'titulo': 'El Caminho: A Breaking Bad Movie', 'ano': 2019, 'diretor': 'Vince Gilligan',
             'drama': 1, 'acao': 0, 'suspense': 1, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0,
             'fantasia': 0})
data.append({'titulo': 'Corpo Fechado', 'ano': 2010, 'diretor': 'M. Night Shyamalan', 'drama': 0,
             'acao': 0, 'suspense': 1, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0,
             'fantasia': 1})
data.append({'titulo': 'A Rede Social', 'ano': 2010, 'diretor': 'David Fincher', 'drama': 1,
             'acao': 0, 'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0,
             'fantasia': 0})
data.append({'titulo': 'O Juiz', 'ano': 2014, 'diretor': 'David Dobkin', 'drama': 1, 'acao': 0,
             'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Ela', 'ano': 2014, 'diretor': 'Spike Jonze', 'drama': 1, 'acao': 0,
             'suspense': 1, 'scifi': 1, 'terror': 0, 'romance': 1, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Karate Kid', 'ano': 2010, 'diretor': 'Harald Zwart', 'drama': 1, 'acao': 1,
             'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Vingadores 2 - A Era de Ultron', 'ano': 2015, 'diretor': 'Joss Whedon',
             'drama': 0, 'acao': 1, 'suspense': 0, 'scifi': 1, 'terror': 0, 'romance': 0,
             'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Logan', 'ano': 2017, 'diretor': 'James Mangold', 'drama': 1, 'acao': 1,
             'suspense': 0, 'scifi': 1, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Nascido para Matar', 'ano': 1987, 'diretor': 'Stanley Kubrick', 'drama': 1,
             'acao': 0, 'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Corra!', 'ano': 2017, 'diretor': 'Jordan Peele', 'drama': 0, 'acao': 0,
             'suspense': 1, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Rambo', 'ano': 1982, 'diretor': 'Ted Kotcheff', 'drama': 1, 'acao': 1,
             'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'O Lado Bom da Vida', 'ano': 2012, 'diretor': 'David O. Russel', 'drama': 1,
             'acao': 0, 'suspense': 1, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})
data.append({'titulo': 'Harry Potter e o Calice de Fogo', 'ano': 2005, 'diretor': 'Mike Newell',
             'drama': 0, 'acao': 0, 'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0,
             'comedia': 0, 'fantasia': 1})
data.append({'titulo': 'Homem Aranha', 'ano': 2002, 'diretor': 'Sam Raimin', 'drama': 0,
             'acao': 1, 'suspense': 0, 'scifi': 0, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 1})
data.append({'titulo': 'Jurassic Park', 'ano': 1993, 'diretor': 'Steven Spielberg', 'drama': 0,
             'acao': 0, 'suspense': 0, 'scifi': 1, 'terror': 0, 'romance': 0, 'comedia': 0, 'fantasia': 0})

database = pd.DataFrame(data=data)
database.to_csv('data\\movies.csv', sep=';') # Gera arquivo CSV contendo a base

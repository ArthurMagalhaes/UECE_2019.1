import re
import random

def match(poly1, poly2):
    # A primeira entrada é um dicionário com as chaves da forma x^n, para n natural, 
    # e os valores sendo os respectivos coeficientes, do primeiro polinômio.
    # A segunda entrada é uma lista com as raízes do segundo polinônmio.
    
    t = 0
    
    while t < 10:
        if len(poly1) != len(poly2) + 1:
            return 'Não'
        grau = len(poly2)
        alfa = random.randint(1, 100 * grau):    
        res1 = 0
        res2 = 1
        for k, v in poly1.items():
        exp = int(re.search('[0-9]+', k, re.IGNORECASE))
        res1 += v * alfa ** exp
    
        for r in poly2:
            res2 = res2 * (alfa - r)
    
        if res1 != res2:
            return 'Não'
        
        t += 1
    
    return 'Sim'
    
def polynomyParse(): # Em desenvolvimento.
    extendido = input('Digite um polinômio (em uma variável) em sua forma extendida (omita os coeficientes nulos e ligue a variável ao expoente por um acento circunflexo): ')
    fatorado = input('Digite um polinômio (em uma variável) em sua forma fatorada (não esqueça os parênteses e não deixe espaço entre os fatores): ')
    
    poly1 = {} # Dicionário
    poly2 = [] # Lista
    
    zeros = fatorado.count(')x(') + fatorado.count('(X)')
    for i in range(0, zeros):
        poly2.append(0)
        

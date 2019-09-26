import re
import random


def match(poly1, poly2):
    # A primeira entrada é um dicionário com as chaves da forma x^n, para n natural, 
    # e os valores sendo os respectivos coeficientes, do primeiro polinômio.
    # A segunda entrada é uma lista com as raízes do segundo polinônmio.
    
    t = 0
    
    valores = []
    while t < 10:
        if len(poly1) != len(poly2) + 1:
            return 'Não'
        grau = len(poly2)
        alfa = random.randint(1, 100 * grau)   
        res1 = 0
        res2 = 1
        valores.append(alfa)
        
        for k, v in poly1.items():
            exp = int(re.search('[0-9]+', k, re.IGNORECASE).group(0))
            res1 += v * alfa ** exp
    
        for r in poly2:
            res2 = res2 * (alfa - r)
    
        if res1 != res2:
            return 'Não', valores
        
        t += 1
    
    return 'Sim', valores
 
 
def polynomyParsev1(): # Em desenvolvimento.
    extendido = input('Digite um polinômio (em uma variável) em sua forma extendida (omita os coeficientes nulos e ligue a variável ao expoente por um acento circunflexo): ')
    fatorado = input('Digite um polinômio (em uma variável) em sua forma fatorada (não esqueça os parênteses e não deixe espaço entre os fatores): ')
    
    poly1 = {} # Dicionário
    poly2 = [] # Lista
    
    zeros = fatorado.count(')x(') + fatorado.count('(X)')
    for i in range(0, zeros):
        poly2.append(0)
        

def polynomyParsev2(): 
    n = int(input('Digite o grau dos polinômios:'))
	
    poly1 = {} # Dicionário
    poly2 = [] # Lista
	
    for i in range(n, -1, -1):
        if (i < n) and (i > 0):
            poly1['x^{}'.format(i)] = int(input('Digite o coeficiente de grau {} do primeiro polinômio: '.format(i)))
        elif i == n:
            poly1['x^{}'.format(i)] = int(input('Digite o coeficiente dominante do primeiro polinômio: '))
        else:
            poly1['x^{}'.format(i)] = int(input('Digite o termo independente do primeiro polinômio: '))
    
    print('\n')
    for i in range(1, n + 1):
        poly2.append(int(input('Digite a {}ª raíz do segundo polinômio: '.format(i))))
    
    return poly1, poly2


p1, p2 = polynomyParsev2()
d, l = match(p1, p2)

print(d, l)

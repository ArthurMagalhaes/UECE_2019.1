import re
import random


def match(poly1, poly2, factor=1):
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
        res2 = factor # Coeficiente dominante.
        valores.append(alfa)
        
        for k, v in poly1.items():
            exp = int(re.search('[0-9]+', k, re.IGNORECASE).group(0)) # Seleciona o grau do monômio.
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
	
    for i in range(n, -1, -1): # Preenche um dicionário tendo a expressão "x^", seguida pelo grau do monômio, como chave e o respectivo coeficiente, do primeiro polinômio, como valor.
        if (i < n) and (i > 0):
            poly1['x^{}'.format(i)] = int(input('Digite o coeficiente de grau {} do primeiro polinômio: '.format(i)))
        elif i == n:
            poly1['x^{}'.format(i)] = int(input('Digite o coeficiente dominante do primeiro polinômio: '))
        else:
            poly1['x^{}'.format(i)] = int(input('Digite o termo independente do primeiro polinômio: '))
    
    print('\n')
    for i in range(1, n + 1): # Preenche uma lista com as raízes do segundo polinômio.
        poly2.append(int(input('Digite a {}ª raíz do segundo polinômio: '.format(i))))
	
    factor = 0
    if input('Deseja multiplicar por algum fator? [s/n] ') == 's':
        while factor == 0:
            factor = int(input('Digite o fator (não nulo): ')) # Não aceita o polinômio nulo.
            if factor == 0:
                print('Valor inválido!! Digite novamente: ')
    else:
        factor = 1
    
    return poly1, poly2, factor


def showPolynomys(poly1, poly2, factor=1):
    extended = ''
    factored = ''
    
    for k, v in poly1.items():
        if int(re.sub('\D', '', k)) > 1: # Remove os caracteres não numéricos.
            if (v != 1) and (v != 0):
                extended += (str(v)+ k + ' + ') # Concatenação dos monômios.
            elif v == 1:
                extended += (k + ' + ')
            else:
                pass # Quando v for zero, a string não será alterada. 
        elif int(re.sub('\D', '', k)) == 1:
            if (v != 1) and (v != 0):
                extended += (str(v) + 'x') 
            elif v == 1:
                extended += ('x')
            else:
                pass
        else:
            if v != 0:
                extended += (' + ' + str(v))
            else:
                if extended[-2:] == '+ ':
                    extended = extended[:-2] # Remove o último "+ ".
        
    extended = extended.replace('  + ', ' ')
               
    if factor != 1:
        if poly2[0] > 0:
            factored += '({}x - {})'.format(factor, factor*poly2[0])
        elif poly2[0] < 0:
            factored += '({}x + {})'.format(factor, abs(factor*poly2[0]))
        else:
            factored += '({}x)'.format(factor)
    else:
        if poly2[0] > 0:
    	    factored += '(x - {})'.format(poly2[0])
        elif poly2[0] < 0:
            factored += '(x + {})'.format(abs(poly2[0]))
        else:
    	    factored += '(x)'
    
    for r in poly2[1:]: # Começa a iteração à partir da segunda raíz.
        if r > 0:
    	    factored += '(x - {})'.format(r)
        elif r < 0:
            factored += '(x + {})'.format(abs(r))
        else:
            factored += '(x)'
       
    print('O primeiro polinômio é ' + extended)
    print('O segundo polinômio é ' + factored, end='\n\n')


p1, p2, dom = polynomyParsev2()
d, l = match(p1, p2, dom)
showPolynomys(p1, p2, dom)
print(d, l)

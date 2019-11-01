

def ex_01(a, b):
    
    result = 0
    if a > b:
        a, b = b,a
    
    if a % 2 == 1:
        result += b
        a -= 1
	
    while a > 1:
        while a % 2 == 0:
            a = a / 2
            b = 2 * b
        
        if a == 1:
            break

        if a % 2 == 1:
            result += b
            a -= 1
            a = a / 2
            b = 2 * b
	
    return result + b
        
a = int(input('Digite um inteiro positivo:'))
b = int(input('Digite outro inteiro positivo:'))

s = ex_01(a,b)
print(s)


def ex_04(obj, cap):
n = len(obj)
aux = []
for i in range(0, n):
aux.append(0)

matrice = aux * n

for i in range(0, n):
for j in range(0, n):
if obj.values()[i]['weight'] < cap and 


# Fonction qui convertit une nombre entier décimal en base b
def Base10ToB(nb10 : int, b : int) -> str :
    nb10 = int(nb10)
    res = ''
    
    while nb10 != 0 :
        r = nb10%b
        nb10 = nb10//b
        res = str(r) + res
    
    return res

def BaseBTo10(nbB : str, b : int) -> int :
    res = 0
    l = len(nbB)
    
    for i in range(l) :
        res += int(nbB[i]) * b ** (l-i-1)
        
    return res

nb10 = int(input('Entrez un nombre en base 10 : '))
b = int(input('Entrez une base b compris entre 2 et 9 inclus : '))
while b < 2 or b > 9 :
    b = int(input('Entrez une base b compris ENTRE 2 ET 9 INCLUS : '))
    
print('Nombre en base', b,":",Base10ToB(nb10, b))
print()

b = int(input('Entrez une base b compris entre 2 et 9 inclus : '))
while b < 2 or b > 9 :
    b = int(input('Entrez une base b compris ENTRE 2 ET 9 INCLUS : '))
    
nbB = input('Entrez un nombre en base b (entré précedemment) : ')

print('Nombre en base 10 :', BaseBTo10(nbB, b))

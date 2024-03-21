#Q1

def Base10To2(n : int or str) -> int :
    assert n >= 0, "Erreur entrée : entier naturel attendu"
    assert isinstance(n,(int,str)), "Erreur entrée : type entier ou chaine de caractère attendu"


    """
    Fonction qui convertit un nombre décimal en nombre binaire

    Entrées
    -------
    n (int ou str) : nombre décimal

    Sorties
    -------
    res (int) : nombre binaire
    """
    n = int(n)
    res = ''

    while n > 0  :
        r = n%2
        n = n//2

        res = str(r) + res

    return int(res)

# nbD = int(input("Entrez un entier en base 10 : "))

# print(decimalVersBinaire(nbD))

#Q2

def Base2To10(n : (int, str)) -> int :
    assert n >= 0, "Erreur entrée : entier naturel attendu"
    assert isinstance(n,(int,str)), "Erreur entrée : type entier ou chaine de caractère attendu"

    """
    Fonction qui convertit un nombre binaire en nombre décimal

    Entrées
    -------
    n (int ou str) : nombre binaire

    Sorties
    -------
    res (int) : nombre décimal
    """
    n = str(n)
    res = 0

    for i in range(len(n)) :
        res += int(n[i]) * 2**(len(n)-i-1)

    return res


# nbB = int(input("Entrez un nombre en base 2 : "))

# print(Base2To10(nbB))

#Q3

listeDecimal = [i for i in range(1, 26)]
# print(listeDecimal)
listeBinaire = []

for nombre in listeDecimal :
    listeBinaire.append(Base2To10(nombre))

# print(listeBinaire)

listeRes = []

for nombre in listeBinaire :
    listeRes.append(Base2To10(nombre))

# print(listeRes)



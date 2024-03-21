def Base10To16(nb10 : int) -> str :
    """_summary_

    Args:
        nb10 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    res = ''

    while nb10 > 0  :
        r = nb10%16
        nb10 = nb10//16
        if r in correspondanceB10B16.keys() :
            res = correspondanceB10B16[r] + res
        else :
            res = str(r) + res

    return res

correspondanceB10B16 = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
correspondanceB16B10 = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}

# nbD = int(input("Entrez un entier en base 10 : "))
# print(Base10To16(nbD))


def Base16To10(nb16 : str) -> int :
    res = 0

    for i in range(len(nb16)) :
        nombre = nb16[i]

        if nombre in correspondanceB16B10.keys() :
            nombre = correspondanceB16B10[nombre]

        res += int(nombre) * 16 **(len(nb16)-i-1)

    return res

# nbB = input("Entrez un nombre en base 16 : ")

# print(Base16To10(nbB))


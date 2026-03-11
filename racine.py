PRECISION=11
def mth2(x,n=2):
    """
    n-ième carré méthode 2
    si base plus petite que 2, erreur
    si x négatif avec base paire, erreur
    si x négatif avec base impaire, signe négatif gardé
    si x==0, retourne 0.0
    i, valeur initiale
    j, incrémentation initiale
    x plus petit que 1, j=0.1
    boucle for, refaire le calcul
    boucle while, ajoute j tant que i**n<=x
    i-=j, compensation
    j/=10, plus petite incrémentation
    """
    if n<2:
        raise ValueError("La base doit être supérieure ou égale à 2")
    if x<0:
        if n==2:
            raise ValueError("La racine carrée d'un nombre négatif est impossible")
        if n%2==0:
            raise ValueError("La racine d'un nombre négatif est possible uniquement avec une base impaire")
    if x==0:
        return 0.0
    i=0
    j=1
    if 0<x<1:
        j=0.1
    for _ in range(PRECISION+2):
        while i**n<=x:
            i+=j
        i-=j
        j/=10
    return round(i,PRECISION)

def mth1(x,n=2):
    """
    n-ième carré méthode 1
    base plus petite que 2=erreur
    x négatif base paire=erreur
    x négatif base impaire,signe négatif gardé
    x==0 , retourne 0.0
    x>=1 , bornes=0 et x
    x<1 , bornes=x et 1
    while !=, réduction des bornes
    millieu , moyenne de mini et maxi
    millieu**n<x , mini=millieu
    """
    if n<2:
        raise ValueError("La base doit être supérieure ou égale à 2")
    if x<0:
        if n==2:
            raise ValueError("La racine carrée d'un nombre négatif est impossible")
        if n%2==0:
            raise ValueError("La racine d'un nombre négatif est possible uniquement avec une base impaire")
    if x==0:
        return 0.0
    if x>=1:
        mini,maxi=(0,x)
    else:
        mini,maxi=(x,1)
    while round(mini,PRECISION)!=round(maxi,PRECISION):
        millieu=(maxi+mini)/2
        if millieu**n<x:
            mini=millieu
        else:
            maxi=millieu
    return round(mini,PRECISION)

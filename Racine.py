
def code():
    """
    sous forme de fonction pour éviter les répétions.
    x=-1 pour crée les conditions de la boucle
    Tant que x est plus petit à zero(True car la variable “x" commence à -1 ).
    Tant que la ligne 13 est vraie le programme va demander a l'utillisateur de entrer un nombre.
    ici float(input("")) est utilliser pour convertir la saise de string en nombre décimale.
    ValueError se produit si vous envoyez une chaîne(str) dans une Variable qui nécessite un nombre(int ou float).
    print() Affiche le message lorsque ValueError est rencontré.Tant que la valeur de “x" est un str() le programme recommence et demande à l'utillisateur pour la radicante.
    return x puisque quand je fais fonction(code()), la valeur saise de l'utillisateur est utillisé
    """
    x=-1
    while x<0:
        try:
            x=float(input("Entrer une valeur positive pour la Radicante: "))
            if x<0:
                print("Entrer un NOMBRE POSITIF pour la Radicante!")
        except ValueError:
            print("Entrer un NOMBRE VALIDE!")
    return x


def mth2(x):
    """
    MÉTHODE 2
    mettre le calcul sous forme de fonction pour avoir une forme plus flexible pour l'utilliser plus tard pour la comparaison
    La valeur initale de la racine carré du nombre "x"(puisque 0 est la plus petite valeur possible).
    La valeur de l'incrémentation initale utilisé et ajouté a “x" pour calculer la racine carré.
    Une boucle qui va calculer a main la racine carré en ajoutant les incrementation, dans ce cas elle boucle 15 fois pour calculer 14 décimales.
    Tant que le carré de la valeur de “i" est plus petit ou égale à “x" (exemple:0**2<=8, True)
    L'incrémentation est ajouté a la valeur initiale (i=0+1), puis ceci est répété tant que i**2<=x
    Puisque i+=j est répété jusqu'a ce que "i**2">x,la valeur de "i" est augmenté de +j. Il faut compenser en soutraiant i avec j Pour recomencer avec une borne minimale.
    Divise l'incrementation de 1 par 10 pour obtenir une plus petit incrementation (0.10) pendant le prochain cycle.
    La valeur retourné lorsque mth1(x) est imprimé
    """
    i=0
    j=1
    for _ in range(10):
        while i**2<=x:
            i+=j

        i-=j
        j/=10
    return i


print(f"La racine carré est de {mth2(code()):.4f}.")

def mth1(x):
    """
    MÉTHODE 1
    même motif que méthode 1 et pour le mettre sous format fonction.
    if et else pour séparer au cas si x est une valeur sous 1
    on défini les valeur minimum(mini) et maximum(maxi) puisque si on utillise x=(0,x) ou x=(x,1) on obiten un tuple et on peut pas changer individuelement les valeur a l'interrieur.
    borne si x est plus petit que 1
    boucle infini avec while True pour refaire les calculs jusqu'à ce que les deux bornes donnent le même résultat une fois arrondi à 4 décimales.
    arrondi_mini et arrondi_maxi sont calculé dans la boucle pour comparer mini et maxi après chaque changement des bornes.
    si arrondi_mini est égale à arrondi_maxi, la boucle s'arrête et retourne la valeur arrondie.
    millieu qui calcule la moyenne est inclus dans la boucle et non a l'exterieur car la valeur de millieu change a chaque fois que une boucle est complété
    pour réduire la borne
    """
    if x>=1:
        mini,maxi=(0,x)
    else:
        mini,maxi=(x,1)

    while True:
        arrondi_mini=round(mini,4)
        arrondi_maxi=round(maxi,4)

        if arrondi_mini==arrondi_maxi:
            return arrondi_mini

        millieu=(maxi+mini)/2
        if millieu**2<x:
            mini=millieu
        elif millieu**2>=x:
            maxi=millieu
print(f"La racine carré est de {mth1(code()):.4f}.")

accu=10
def mth2(x):
    """
    MÉTHODE 2
    if x<0, la racine  n'est pas possible dans les nombres réels, donc retourne une erreur.
    if x==0, la racine est 0.0 donc la fonction retourne 0.
    i est la valeur initiale de la racine du nombre x puisque 0 est la plus petite valeur possible.
    j est la valeur de l'incrémentation initiale utillisé et ajouté a i(la variable) pour calculer la racine
    if x est plus petit que 1, l'incrementation commence à 0.1 pour mieux fonctionner avec les nombres décimaux.
    for est pour refaire le calcul selon la précision par la variable globale accu.
    while ajoute l'incrémentation tant que i**2 est plus petit ou égale à x
    quand i**2 dépasse x, il faut compenser en soustraiant j pour revenir à la dernière valeur valide.
    j est divisé par 10 pour obtenir une plus petite incrémentation pour le prochain cycle.
    i est arrondi selon accu.
    """
    if x<0:
        raise ValueError("La racine carrée d'un nombre négatif est impossible")
    if x==0:
        return 0
    i=0
    j=1
    for _ in range(accu+2):
        while i**2<=x:
            i+=j
        i-=j
        j/=10
    return round(i,accu)

def mth1(x):
    """
    MÉTHODE 1
    if et else est utilisé pour séparé si x est une valeur plus grande ou plus petite que 1
    mini et maxi puisque si on utillise x=(0,x) ou x=(x,1) on obttient un tuple et on peux pas changer individuelement les valeurs à l'interrieur.
    si x>=1 les bornes initiales sont 0 et x.
    si x<1 les bornes initiales sont x et 1
    while True utilisé pour faire les calculs jusqu'à ce que les deux bornes donnent le même résultat une fois arrondi selon la précision demandé.
    arrondi_mini et arrondi_maxi sont calculé dans la boucle pour comparer mini et maxi après chaque changement des bornes.
    si arrondi_mini = à arrondi_maxi, la boucle s'arrête et retourne la valeur arrondie
    millieu calcule la moyenne entre maxi et mini et il est inclus dans la boucle car sa valeur change à chaque fois que la boucle est complété.
    if millieu**2<x, on déplace la borne minimum.
    """
    if x<0:
        raise ValueError("La racine carrée d'un nombre négatif est impossible")
    if x==0:
        return 0
    if x>=1:
        mini,maxi=(0,x)
    else:
        mini,maxi=(x,1)
    while True:
        arrondi_mini=round(mini,accu)
        arrondi_maxi=round(maxi,accu)
        if arrondi_mini==arrondi_maxi:
            return arrondi_mini
        millieu=(maxi+mini)/2
        if millieu**2<x:
            mini=millieu
        elif millieu**2>=x:
            maxi=millieu

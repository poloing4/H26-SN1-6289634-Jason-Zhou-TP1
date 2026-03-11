import math
import racine
import time
import random

def test(y):
    """
    start avant la boucle pour enregistrer la valeur du temps de début.
    nombre de fois que le calcul de racine carré est calculé.
    assigne une valeur aléatoire différente a chaque fois pendant la boucle.
    quand la boucle fini le système enrengistre une autre valeur du temps.
    pour trouver combien de temps est passé on fait simplement la différence.
    puisque les valeur de temps son enregistré en seconde on multiplie par 1000 pour convertir en miliseconde.
    le temps moyen est calculé en divisant le temps total par 10 000.
    multiplié par 1000 pour convertir en miliseconde. Pour obtenir une valeur quand on utilise test on retourne les valeur choisi.
    test(racine.mth) mis dans a,b et c pour facilité les calculs de temps moyen
    """
    start=time.time()
    for _ in range(10000):
        x=random.uniform(0,1000)
        y(x)
    end=time.time()
    elapsed=end-start
    moy=(elapsed*1000)/10000
    return elapsed*1000
a=test(racine.mth1)
b=test(racine.mth2)
c=test(math.sqrt)
print(f"Méthode 1 (dichotomie)          : Temps total = {round(a)} (ms),Temps moyen = {(a/10000):.5f} ms")
print(f"Méthode 2 (chiffre par chiffre) : Temps total = {round(b)} (ms),Temps moyen = {(b/10000):.5f} ms")
print(f"Méthode 3 (math.sqrt)           : Temps total = {round(c)} (ms),Temps moyen = {(c/10000):.5f} ms")

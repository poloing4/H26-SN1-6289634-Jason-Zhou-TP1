
import racine

print("*** VÉRIFICATION DU BON FONCTIONNEMENT DE LA MÉTHODE [mth1] LORS DU CALCUL D'UNE racine CARRÉE ***")
print("attendu : 0.0 ")
print(" obtenu :", racine.mth1(0))
print("attendu : 0.31622776601683794")
print(" obtenu :", racine.mth1(0.1))
print("attendu : 0.4472135954999579")
print(" obtenu :", racine.mth1(0.2))
print("attendu : 0.9486832980505138")
print(" obtenu :", racine.mth1(0.9))
print("attendu : 2.8284271247461903")
print(" obtenu :", racine.mth1(8))
print("attendu : 3.0")
print(" obtenu :", racine.mth1(9))
print("attendu : 9.0")
print(" obtenu :", racine.mth1(81))
print("attendu : 11.090536506409418")
print(" obtenu :", racine.mth1(123))
print("attendu : 31.606961258558215")
print(" obtenu :", racine.mth1(999))

print("*** VÉRIFICATION DES PARAMÈTRES DE LA MÉTHODE [mth1] LORS DU CALCUL D'UNE racine CARRÉE ***")
try:
    print("Erreur attendue : La racine carrée d'un nombre négatif est impossible")
    racine.mth1(-3)
except ValueError as e:
    print(f"Erreur obtenue : {e}")


print("*** VÉRIFICATION DU BON FONCTIONNEMENT DE LA MÉTHODE [mth2] LORS DU CALCUL D'UNE racine CARRÉE ***")
print("attendu : 0.0 ")
print(" obtenu :", racine.mth2(0))
print("attendu : 0.31622776601683794")
print(" obtenu :", racine.mth2(0.1))
print("attendu : 0.4472135954999579")
print(" obtenu :", racine.mth2(0.2))
print("attendu : 0.9486832980505138")
print(" obtenu :", racine.mth2(0.9))
print("attendu : 2.8284271247461903")
print(" obtenu :", racine.mth2(8))
print("attendu : 3.0")
print(" obtenu :", racine.mth2(9))
print("attendu : 9.0")
print(" obtenu :", racine.mth2(81))
print("attendu : 11.090536506409418")
print(" obtenu :", racine.mth2(123))
print("attendu : 31.606961258558215")
print(" obtenu :", racine.mth2(999))

print("*** VÉRIFICATION DES PARAMÈTRES DE LA MÉTHODE [mth2] LORS DU CALCUL D'UNE racine CARRÉE ***")
try:
    print("Erreur attendue : La racine carrée d'un nombre négatif est impossible")
    racine.mth2(-3)
except ValueError as e:
    print(f"Erreur obtenue : {e}")
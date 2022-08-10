# -*- coding: utf-8 -*-
"""
@author: flashY Coding
"""

# ------------------------------ Les Variables ------------------------------ #

# 1 : Les principaux types de variables en Python

# int : les entiers
a = 2

# float : les nombres 'flotants' (décimaux, à virgule)
b = 1.5

# string : les chaînes de caractères
c = "Hello, World!"

# list : Les listes qui en Python permettent de posséder plusieurs int, float, str et même 
# d'autres listes etc... dans un seul endroit
d = [1,"Tuto",b,[3,4.768]]


""" Quelques opérations de bases pour les nombres (int et float) : """

# L'addition et la soustraction :
a = a + 2 # ou a += 2 (plus court) --> Donne a = 4
a = a - 2 # ou a -= 2 (plus court) --> Donne a = 2

# La multiplication et la division :
a = a*8 # ou a *= 8 (plus court) --> Donne a = 16
a = a/4 # ou a /= 4 (plus court) --> Donne a = 4.0 (float)

# Les puissances, la division entière et le modulo:
a = a**3 # ou a **= 3 (plus court) --> Donne a = 64
a = a//6 # ou a //= 6 (plus court) --> Donne a = 10 (au lieu de 10.6666...)
a = a%6 # ou a %= 6 (plus court) --> Donne a = 4 (reste de la division de a par 4)


""" Quelques opérations de base pour les chaînes de caractères (str) : """

# Concaténation de chaîne de caractères
e = "How are you ?"
f = c + " " + e # f est donc égal à "Hello, World! How are you ?"

# De plus, il existe des fonctions pour travailler avec ces chaînes de caractères :
f.capitalize() # Premier caractère en majuscule et le reste en minuscule
f.lower() # Tous les caractères en minuscule
f.upper() # Tous les caractères en majuscule
f.count("o") # Renvoie le nombre d'occurences de "o" dans la chaîne de caractère en question
f.find("y") # Renvoie l'indice (l'emplacement) de y dans f

""" Quelques opérations de base / fonctions pour les listes (list) : """

# Concaténation de listes :
g = [1,2]
h = [3,4]
i = g + h
print(i) # Affiche --> [1,2,3,4]

# De plus, il existe des fonctions pour travailler avec ces listes :
print(len(i)) # Affiche la longueur de la liste i (ici 4)

# Les listes fonctionnent avec des indices allant de 0 (le premier élément) à
# la longueur de la liste - 1 (le dernier élément) :
print(i[0],i[3]) # Affiche le premier et dernier élément de i : 1 et 4

# Voici d'autres fonctions utiles pour les listes en Python :
i.append(5) # Ajoute 5 à la fin de la liste en question (ici i)
i.remove(4) # Supprime la première occurence de 4 dans la liste en question
i.pop() # Supprime et renvoie le dernier élément de i
i.clear() # Supprime tout ce qu'il y a dans la liste en question
i.count(3) # Renvoie le nombre d'occurences de 3 dans la liste en question


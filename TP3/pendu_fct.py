'''
MARTIN TIMEO   
02/10/2025
OBJ:
'''
import random as rd
import


liste_mot=[]

def choix():
    with open("mots.txt", "r") as file:
        texte = file.read()
        mots = list(map(str, texte.split()))
        choisi = rd.choice(mots)
    return choisi


def affichage (liste) : 
    chaine = ''
    for tuple in liste : 
        if tuple[1] == '_' : 
            chaine += '_'
        else : 
            chaine += str(tuple[0])
    return chaine

def pendu (mot) : 
    l=[[mot[0],mot[0]]]
    for i in range (0,len (mot) - 1 ) : 
        l.append([mot[i+1],'_'])


    tent_restante=8
    while tent_restante != 0 : 
        print(f" il vous reste {tent_restante} tentatives")
        print(affichage(l))
        lettre = str(input('Lettre à tester : '))
        if lettre not in mot :
            tent_restante-=1
        for sous_liste in l : 
            if lettre == sous_liste[0] :
                sous_liste[1] = lettre



        n=0
        for i in range(len(l)) : 
            if l[i][0]==l[i][1] : 
                n+=1
        if n == len(l) :
                return 'vous avez gagné'
    return 'vous avez perdu, le mot était :', mot




print(pendu(choix()))
# print(affichage([('a','_') , ('t','t')]))
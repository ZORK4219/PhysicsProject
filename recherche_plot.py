#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt


intensty={}
wavelength={}

s=sys.argv[1]
s1=s.split(">")[0].split("\n")
s1=s1[:-1] #pour eviter l'espace à la fin sinon il y aura une ligne qu'on pourra pas split
s2=s.split(">")[1].split("\n")
s2=s2[1:] #meme commentraire mais au debut


for ligne_wave, ligne_int in zip(s1, s2):
          
          tmp=ligne_wave.split("\t")[1] #je prends la deuxieme partie de la ligne qu'est les intensites
          sous_chaines = tmp.split() #je decompose les valeurs de longeurs d'onde car c'est une suite de nombre (en forme de chaine pour l'instant) mais pas dans une liste
          liste_nombres = [float(nombre) for nombre in sous_chaines] # je prends chaque chiffre dans la suite precedente et je le mets dans ma liste comme float
          if (liste_nombres[0]==0): #c'est juste pour ne pas avoir le zero qui fait partie du fichier de depart car le dessin est moche
            liste_nombres.remove(0)
          wavelength.update([(ligne_wave.split("\t")[0],liste_nombres)])  #je remplis mon tableau
           
          tmp=ligne_int.split("\t")[1] #exactement la meme chose pour les intensites
          sous_chaines = tmp.split()
          liste_nombres = [float(nombre) for nombre in sous_chaines]
          if (liste_nombres[0]==0):
            liste_nombres.remove(0)
          intensty.update([(ligne_int.split("\t")[0],liste_nombres)])
          



fig, ax = plt.subplots() #je cree ma figure


val1=sys.argv[2] #je recupere les valeurs de debut et fin d'interval
val2=sys.argv[3]

for clef in wavelength:
        if (clef==str(val1)+"--"+str(val2)): #si les deux valeurs matchent exactement un interval qui existe deja on affiche la figure correspondante
          x= wavelength[clef]
          y= intensty[clef]
          
          ax.plot(x,y,label="I(w)")
          ax.set_title('Fenetre :'+" "+clef+" nm",fontsize = 14, fontweight ='bold')
          ax.set_xlabel("Wavelength (nm)",style='italic') 
          ax.set_ylabel("Intensity (kicks)",style='italic') 
          ax.legend()

          plt.show()
          print(clef.split("--"))
          break
       #ce pendant si ce n'est pas le cas alors on prend la valeur de la premiere borne on cherche dans quel inerval elle fait partie
       #puis on prend la deuxieme on fait la meme chose, puis on prend les deux intervale et on les affiche
        elif(int(float(clef.split("--")[0]))<=int(float(val1)) and int(float(clef.split("--")[1]))>int(float(val1))): #si la premiere borne est contenue dans un intevale on le prend
              x= wavelength[clef]
              y= intensty[clef]
              
        elif(int(float(clef.split("--")[0]))<=int(float(val2)) and int(float(clef.split("--")[1]))>int(float(val2))): #si la deuxieme est contenue dans un autre intervale on ajoute les deux intervales
              x+=wavelength[clef]
              y+=intensty[clef]
              
              ax.plot(x,y,label="I(w) original")
              ax.set_title('Fenetre :'+" "+clef+" nm",fontsize = 14, fontweight ='bold')
              ax.set_xlabel("Wavelength (nm)",style='italic') 
              ax.set_ylabel("Intensity (kicks)",style='italic') 
              ax.legend()

              plt.show()
              break
            
              
            
#marche ok


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt


intensty={}
wavelength={}

s=sys.argv[1]
s1=s.split(">")[0].split("\n")
s1=s1[:-1] #because an empty space appears in the end, we get red ot it to be able to split
s2=s.split(">")[1].split("\n")
s2=s2[1:] #there's same issue but in the begining of the list


for ligne_wave, ligne_int in zip(s1, s2):
          
          tmp=ligne_wave.split("\t")[1] #we take the second part of the line which is the wavelength data
          sous_chaines = tmp.split() #we split the values which are spaced with an empty space then this gives us a list of strings

          liste_nombres = [float(nombre) for nombre in sous_chaines] # we take the list of data as strings here and transform each one to float
          if (liste_nombres[0]==0): # I delete the first value which is zero because it makes th graph look ugly 
            liste_nombres.remove(0)
          wavelength.update([(ligne_wave.split("\t")[0],liste_nombres)])  #HERE WE HAVE OUR DICTIONARY
           
          tmp=ligne_int.split("\t")[1] #exact same thing with intensities
          sous_chaines = tmp.split()
          liste_nombres = [float(nombre) for nombre in sous_chaines]
          if (liste_nombres[0]==0):
            liste_nombres.remove(0)
          intensty.update([(ligne_int.split("\t")[0],liste_nombres)])
          



fig, ax = plt.subplots() #create plot figure


val1=sys.argv[2] #Boundary values
val2=sys.argv[3]

for clef in wavelength:
        if (clef==str(val1)+"--"+str(val2)): #if the given interval mathes one existing interval we plot it and break
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
       #However, if it's not the case, we take first value and see in which interval in belongs, and we save that interval
       #we do the same thing with the second value, and take this interval with the previous one and plot
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


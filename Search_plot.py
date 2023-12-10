#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def moy(x):
     return sum(x[:])/len(x)


# Fonction à appeler lorsque le bouton est pressé



intensty={}
wavelength={}

s=sys.argv[1]
s1=s.split(">")[0].split("\n")
s1=s1[:-1] #because an empty space appears in the end, we get red ot it to be able to split
s2=s.split(">")[1].split("\n")
s2=s2[1:] #there's same issue but in the begining of the list


for line_wave, line_int in zip(s1, s2):
          
          tmp=line_wave.split("\t")[1] #we take the second part of the line which is the wavelength data
          string_under_list = tmp.split() #we split the values which are spaced with an empty space then this gives us a list of strings

          numbers_list = [float(number) for number in string_under_list] # we take the list of data as strings here and transform each one to float
          if (numbers_list[0]==0): # I delete the first value which is zero because it makes th graph look ugly 
            numbers_list.remove(0)
          wavelength.update([(line_wave.split("\t")[0],numbers_list)])  #HERE WE HAVE OUR DICTIONARY
           
          tmp=line_int.split("\t")[1] #exact same thing with intensities
          string_under_list = tmp.split()
          numbers_list = [float(number) for number in string_under_list]
          if (numbers_list[0]==0):
            numbers_list.remove(0)
          intensty.update([(line_int.split("\t")[0],numbers_list)])
          



fig, ax = plt.subplots() #create plot figure


boundary1=sys.argv[2] #Boundary values
boundary2=sys.argv[3]

for clef in wavelength:
        if (clef==str(boundary1)+"--"+str(boundary2)): #if the given interval mathes one existing interval we plot it and break
          x= wavelength[clef]
          y= intensty[clef]
          
          ax.plot(x,y,label="I(w)")
          ax.set_title('Fenetre :'+" "+clef+" nm",fontsize = 14, fontweight ='bold')
          ax.set_xlabel("Wavelength (nm)",style='italic') 
          ax.set_ylabel("Intensity (kicks)",style='italic') 
          ax.legend()
          break

       #However, if it's not the case, we take first value and see in which interval in belongs, and we save that interval
       #we do the same thing with the second value, and take this interval with the previous one and plot
        elif(int(float(clef.split("--")[0]))<=int(float(boundary1)) and int(float(clef.split("--")[1]))>int(float(boundary1))): #si la premiere borne est contenue dans un intevale on le prend
              x= wavelength[clef]
              y= intensty[clef]
              
        elif(int(float(clef.split("--")[0]))<=int(float(boundary2)) and int(float(clef.split("--")[1]))>int(float(boundary2))): #si la deuxieme est contenue dans un autre intervale on ajoute les deux intervales
              x+=wavelength[clef]
              y+=intensty[clef]
              
              ax.plot(x,y,label="I(w) original")
              ax.set_title('Window :'+" "+clef+" nm",fontsize = 14, fontweight ='bold')
              ax.set_xlabel("Wavelength (nm)",style='italic') 
              ax.set_ylabel("Intensity (kicks)",style='italic') 
              ax.legend()
              break


def on_button_clicked(event):
    plt.text(2, 0.5,"Mean Value:   "+str(moy(y))+"\nMax Value :    "+str(max(y))+"\nMin Value :"+str(min(y)), ha='center', va='center', fontsize=12)
    plt.draw()

plt.subplots_adjust(bottom=0.2)  # Ajuster l'espace en bas pour le bouton

# Position du bouton
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])  # [left, bottom, width, height]

# Création du bouton
button = Button(button_ax, 'Intensity Info')

# Lier la fonction à l'événement "click"
button.on_clicked(on_button_clicked)
            
plt.show()            
            
#marche ok


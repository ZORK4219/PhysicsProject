#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def mean(x):
     return sum(x[:])/len(x)




intensty={}
wavelength={}

s=sys.argv[1]
s1=s.split(">")[0].split("\n")
s1=s1[:-1] #because an empty space appears in the end, we get red ot it to be able to split
s2=s.split(">")[1].split("\n")
s2=s2[1:] #there's same issue but in the begining of the list


for line_wave, line_int in zip(s1, s2):
          
          temporary=line_wave.split("\t")[1] #we take the second part of the line which is the wavelength data
          string_under_list = temporary.split() #we split the values which are spaced with an empty space then this gives us a list of strings
          numbers_list = [float(number) for number in string_under_list] # we take the list of data as strings here and transform each one to float
          wavelength.update([(line_wave.split("\t")[0],numbers_list)])  #HERE WE HAVE OUR DICTIONARY
           
         
          temporary=line_int.split("\t")[1] #exact same thing with intensities
          string_under_list = temporary.split()
          numbers_list = [float(number) for number in string_under_list]
          intensty.update([(line_int.split("\t")[0],numbers_list)])
          



fig, ax = plt.subplots() #create plot figure


boundary1=sys.argv[2] #Boundary values
boundary2=sys.argv[3]

Condition=0 #it's just a random way I used to make sure that in the iteration 
#the first interval is put once and not more and all what comes after is added

first_wavelength_value= int(float(next(iter(wavelength)).split("--")[0])) 
last_wavelength_value= int(float(list(wavelength.keys())[-1].split("--")[1]))
#this is just for checking if the given values are not out of the data interval
if (first_wavelength_value>int(float(boundary1)) or last_wavelength_value < int(float(boundary2) )):
            print("Non valid boundries !")
            sys.exit()

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
        elif(int(float(clef.split("--")[0]))<=int(float(boundary1)) and int(float(clef.split("--")[1]))>int(float(boundary1)) ): #we test where does the first boundry value belong
              x= wavelength[clef]
              y= intensty[clef]
              Condition=1
        elif( int(float(clef.split("--")[1]))<=int(float(boundary2)) and Condition==1):  #we take all intevals until we meet the last one
              x+=wavelength[clef]
              y+=intensty[clef]
             
              

        elif(int(float(clef.split("--")[1]))>=int(float(boundary2)) ): #if we found the interval where the second boundary belongs
              ax.plot(x,y,label="I(w) original")
              ax.set_title('Window :'+" "+boundary1+"--"+boundary2+" nm",fontsize = 14, fontweight ='bold')
              ax.set_xlabel("Wavelength (nm)",style='italic') 
              ax.set_ylabel("Intensity (kicks)",style='italic') 
              ax.legend()
              break

def on_button_clicked(event):
    plt.text(2, 0.5,"Mean Value:   "+str(mean(y))+"\nMax Value :    "+str(max(y))+"\nMin Value :"+str(min(y)), ha='center', va='center', fontsize=12)
    plt.draw()

plt.subplots_adjust(bottom=0.2)  # Add a button in the plot

#Button position
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])  # [left, bottom, width, height]

#Button Creation
button = Button(button_ax, 'Intensity Info')

#making the message appear when the button is clicked
button.on_clicked(on_button_clicked)
            
plt.show()            

#IT WORKS


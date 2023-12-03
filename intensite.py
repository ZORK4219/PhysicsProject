
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,re

#/home/giulio4219/Desktop/Spectre_photoluminescence.txt
def moy(x):
     return sum(x[:])/len(x)

intensty={} #dictionnaire vide pour stockers mes valeurs
wavelength={}
fichier=sys.argv[1]


separeteur=sys.argv[3]

#je prends le premier argument de la commande qu'est le nom du fichier
t=[]#je cree une liste vide pour contenir tout les information 
fd = open( fichier , "r")
for ligne in fd :
     if not re.search( "[A-z]", ligne ) and not re.search( "[+]", ligne ) :
          if "\"" in ligne: #csv
               tmp=ligne.strip().split("\"" )
               del tmp[0:-1:2]; del tmp[-1]
               tmp = list(map(lambda x: x.replace(',', '.'), tmp))
              
          else : #normal
              
               tmp=ligne.strip().split(separeteur)
               
               

          t.append(tmp)
          
a=int(float(t[0][0]))

b=int(float(sys.argv[2]))

intens_tmp=[float(t[0][1])]

wavelength_tmp=[float(t[0][1])]

for i in range (1,len(t)):
    #si on est a 10 on remplit le dictionnaire sinon on remplit la liste des intesite d'une fenetre
    if a+b==int(float(t[i][0])):
         # intens_tmp.append(float(t[i][1])) # pour ajouter la valeur qui correspond au i la sinon il sera pas inclu
          intensty.update([(str(int(a))+"--"+str(int(float(t[i][0]))),intens_tmp)])
          wavelength.update([(str(int(a))+"--"+str(int(float(t[i][0]))),wavelength_tmp)])

          a=int(float(t[i][0]))
          intens_tmp=[]
          wavelength_tmp=[] # pour avoir une nouvelle liste vide et la remplir 
    if i==len(t)-1:
          intens_tmp.append(float(t[i][1]))
          wavelength_tmp.append(float(t[i][0]))#pour ajouter la derniere valeur parce que si i=dernier element on passe plus par le else et du coup on perd la derniere valeur
          intensty.update([(str(int(a))+"--"+str(int(float(t[i][0]))),intens_tmp)])
          wavelength.update([(str(int(a))+"--"+str(int(float(t[i][0]))),wavelength_tmp)])
         
    else:
         intens_tmp.append(float(t[i][1]))
         wavelength_tmp.append(float(t[i][0]))


s=""

for clef in wavelength:
     s+=clef+"\t"+' '.join(map(str, wavelength[clef]))+"\n"

s+=">\n"
for clef in intensty:
     s+=clef+"\t"+' '.join(map(str, intensty[clef]))+"\n"


print(s)
     



#for clef in ext:
 #    print(len(ext[clef]),"  ",moy(ext[clef]),"  ",min(ext[clef])," ",max(ext[clef]),"\n")




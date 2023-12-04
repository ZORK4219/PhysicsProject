
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,re

#/home/giulio4219/Desktop/Spectre_photoluminescence.txt
def moy(x):
     return sum(x[:])/len(x)


intensity={} #empty to dictionaries to stock data
wavelength={}

filelink=sys.argv[1]


separator=sys.argv[3]


t=[]#list to contains data before process

fd = open( filelink , "r")
for ligne in fd :
     if not re.search( "[A-z]", ligne ) and not re.search( "[+]", ligne ) :
          if "\"" in ligne: #csv
               tmp=ligne.strip().split("\"" )
               del tmp[0:-1:2]; del tmp[-1]
               tmp = list(map(lambda x: x.replace(',', '.'), tmp))
              
          else : #normal
              
               tmp=ligne.strip().split(separator)
               
               

          t.append(tmp)

          
a=int(float(t[0][0])) #first wavelength value 

b=int(float(sys.argv[2])) #the step

intens_tmp=[float(t[0][1])]

wavelength_tmp=[float(t[0][1])]

for i in range (1,len(t)):
    #we stock data in lists until i gets to 10 we stock all that in dictionnary
    if a+b==int(float(t[i][0])):
         # intens_tmp.append(float(t[i][1])) # pour ajouter la valeur qui correspond au i la sinon il sera pas inclu
          intensity.update([(str(int(a))+"--"+str(int(float(t[i][0]))),intens_tmp)])
          wavelength.update([(str(int(a))+"--"+str(int(float(t[i][0]))),wavelength_tmp)])

          a=int(float(t[i][0]))
          intens_tmp=[]
          wavelength_tmp=[] # we empty the list to do it again

    if i==len(t)-1:
          intens_tmp.append(float(t[i][1]))
          wavelength_tmp.append(float(t[i][0]))
          #to add the last values because whe it's the last iterration
          #we skip the else and data is not stored
          intensity.update([(str(int(a))+"--"+str(int(float(t[i][0]))),intens_tmp)])
          wavelength.update([(str(int(a))+"--"+str(int(float(t[i][0]))),wavelength_tmp)])
         
    else:
         intens_tmp.append(float(t[i][1]))
         wavelength_tmp.append(float(t[i][0]))


#we create a string to contain the data
#but not in list format, in kind of series of numbers instead
s=""

for clef in wavelength:
     s+=clef+"\t"+' '.join(map(str, wavelength[clef]))+"\n"

s+=">\n"
for clef in intensity:
     s+=clef+"\t"+' '.join(map(str, intensity[clef]))+"\n"


print(s)
     



#for clef in ext:
 #    print(len(ext[clef]),"  ",moy(ext[clef]),"  ",min(ext[clef])," ",max(ext[clef]),"\n")





#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,re

#/home/giulio4219/Desktop/Spectre_photoluminescence.txt



intensity={} #empty to dictionaries to stock data
wavelength={}

filelink=sys.argv[1]

column1=int(float(sys.argv[3])) #which columns does the user want to see
column2=int(float(sys.argv[4]))




data=[]#list to contains data before process

fd = open( filelink , "r")
count_separators=[] # if there's any problem regarding the separator, the code can check if 
                    #there separator was changed between a line and another

                             
for line in fd :
     if line.strip() == '': #if a line is empty we ignore it
           pass
     else :
          if not re.search( "[A-Z]", line ) and not re.search( "[+]", line ) and not  re.search( "[a-z]", line ):
                  #take lines which contain only numbers  

               if "\"" in line: #here we use this trick if were dealing with values stocked inside quotes
                    tmp=line.strip().split("\"" )
                    del tmp[0:-1:2]; del tmp[-1]
                    tmp = list(map(lambda x: x.replace(',', '.'), tmp)) #we replace coma with a point if the numbers are floats and have , instead of .
              #so if the file is organised like this we don'data need to look for the separator
              #ifnot we do the following thing
               else:     
                    for i in line.strip():
                         if  i.isdigit() or i=="." : #if the element in the line is just a number (int or float)we let k=0 
                              separator=0
                              
                         else : #the separator can be anything else other than a letter or a point
                              separator=i
                              count_separators.append(separator)
                              break
          
                    if(separator==0): # here if k stays 0 means there's no separator or the user used "." which is imbigious
                         print("error1")
                         sys.exit() 

                    elif(count_separators[0]!=count_separators[-1]): #here this is used for elegence only to warn the user that it's better to use one separator
                         print("error2")
                         sys.exit()
 
                              
                    else :
                         tmp=line.strip().split(separator)
                         while '' in tmp: #if there's the same separator repeted it creates spaces in the list so we just delete them
                              tmp.remove('')
               data.append(tmp[column1-1:column2:column2-column1]) # storing the wanted data 

          
a=int(float(data[0][0])) #first wavelength value 

b=int(float(sys.argv[2])) #the step

intens_tmp=[float(data[0][1])]

wavelength_tmp=[float(data[0][1])]

for i in range (1,len(data)):
    #we stock data in lists until i gets to 10 we stock all that in dictionnary
    if a+b==int(float(data[i][0])):
         # intens_tmp.append(float(data[i][1])) # pour ajouter la valeur qui correspond au i la sinon il sera pas inclu
          intensity.update([(str(int(a))+"--"+str(int(float(data[i][0]))),intens_tmp)])
          wavelength.update([(str(int(a))+"--"+str(int(float(data[i][0]))),wavelength_tmp)])

          a=int(float(data[i][0]))
          intens_tmp=[]
          wavelength_tmp=[] # we empty the list to do it again

    if i==len(data)-1:
          intens_tmp.append(float(data[i][1]))
          wavelength_tmp.append(float(data[i][0]))
          #to add the last values because whe it's the last iterration
          #we skip the else and data is not stored
          intensity.update([(str(int(a))+"--"+str(int(float(data[i][0]))),intens_tmp)])
          wavelength.update([(str(int(a))+"--"+str(int(float(data[i][0]))),wavelength_tmp)])
         
    else:
         intens_tmp.append(float(data[i][1]))
         wavelength_tmp.append(float(data[i][0]))


#we create a string to contain the data
#but not in list format, in kind of series of numbers instead
s=""

for clef in wavelength:
     s+=clef+"\t"+' '.join(map(str, wavelength[clef]))+"\n"
     #map generates series of numbers as sting from the list
     #then join takes each of these element and adds an empty space 

s+=">\n"
for clef in intensity:
     s+=clef+"\t"+' '.join(map(str, intensity[clef]))+"\n"


print(s)
     



#for clef in ext:
 #    print(len(ext[clef]),"  ",moy(ext[clef]),"  ",min(ext[clef])," ",max(ext[clef]),"\n")





#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,re





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
                    temporary_list=line.strip().split("\"" )
                    del temporary_list[0:-1:2]; del temporary_list[-1]
                    temporary_list = list(map(lambda x: x.replace(',', '.'), temporary_list)) #we replace coma with a point if the numbers are floats and have , instead of .
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
                         temporary_list=line.strip().split(separator)
                         while '' in temporary_list: #if there's the same separator repeted it creates spaces in the list so we just delete them
                              temporary_list.remove('')

               if column1>len(temporary_list) or column2>len(temporary_list): #incase given colums do not exist
                    print("error3")
                    sys.exit()
               else:          
                    data.append(temporary_list[column1-1:column2:column2-column1]) # storing the wanted data 







a=int(float(data[0][0])) #first wavelength value 

b=int(float(sys.argv[2])) #the step

intens_temporary_list=[float(data[0][1])]

wavelength_temporary_list=[float(data[0][1])]
string1=""
string2=""
#we create strings to contain the data
#but not in list format, in kind of series of numbers instead
for i in range (1,len(data)):
    #we stock data in lists until i gets to 10 we stock all that in strings, one for wavelength and one for intensity
    if a+b==int(float(data[i][0])):
          string1+=str(int(a))+"--"+str(int(float(data[i][0])))+"\t"+' '.join(map(str, wavelength_temporary_list))+"\n"
          string2+=str(int(a))+"--"+str(int(float(data[i][0])))+"\t"+' '.join(map(str, intens_temporary_list))+"\n"

          a=int(float(data[i][0]))
          intens_temporary_list=[]
          wavelength_temporary_list=[] # we empty the list to do it again

    if i==len(data)-1:
          intens_temporary_list.append(float(data[i][1]))
          wavelength_temporary_list.append(float(data[i][0]))
          #to add the last values because whe it's the last iterration
          #we skip the else and data is not stored
          string1+=str(int(a))+"--"+str(int(float(data[i][0])))+"\t"+' '.join(map(str, wavelength_temporary_list))+"\n"
          string2+=str(int(a))+"--"+str(int(float(data[i][0])))+"\t"+' '.join(map(str, intens_temporary_list))+"\n"
         
    else:
         intens_temporary_list.append(float(data[i][1]))
         wavelength_temporary_list.append(float(data[i][0]))





#we combain our strings
finalstring=string1+">\n"+string2


print(finalstring)
     






 
# Search and Plot Physics dataFile 

 ## <span style="color: #2ecc71;">A Python-Bash project searching in file and plotting data using matplotlib

This is a school project, that was built for instance to process a txt file containing data about wavelength and intensities, and take out important data to be able to plot it. Every part of this project contains three sample codes which shows how to do the following:

- Using a terminal, a command should excute the Bash program, with adding parameters which are explained using -help.
- The Bash program then verifies if the parameters correspond to the rules(which I impose to stay in context of the physics we're dealing with).

- Then the **Intensity.py** Python programm is called with the given parameters, it searches the file, take out the important data, which in my case was wavelength and light intensities. Then it builts a Python dictionary, for each one of the quantities, and it must return it using print function to Bash programm.

The details about each program will be breifly explained in the next section, and the scripts have already some comments that can guide the user.

## <span style="color: #2ecc71;"> How  does each programm work?

I will give you here a breif idea, in the simplest way possible to see how each one works :

###   <span style="color: #008080;">\- *Bash script* 
 &emsp;&emsp; It start by looking if the user, put -help command, if he did, it dispalys help, or else it starts examining all the parameters to see if they are acceptable or else it exists the programm. If everything is good (file exists, step is positive, more than two columns or not...), then it asks for boundary values to plot the interval (verifies also if there're good to use). It calls **Intensity.py** and store the result in a variable then passes it to **Search.py**, where the programm takes care of the rest to plots the data.

###   <span style="color: #008080;"> \- *Python scripts* 
 <span style="color: #ffd33d; font-weight: bold;">&emsp;&#8226; Intensity.py</span>
 

&emsp;This program searches for the file indicated in the parameters then it starts looking in it using **re** module, we take the data by spliting the line into separate values( the separator here is searched automatically, message error can indicate if the file is strangly written), instead of  building dictionnaries in this stage, (one for wavelength the other for intensities), I create string and put my data inside because it's easier to deal with later. So the values are devided in windows by a step of integer passed as parameter. I think there are many better ways to do what I did but it was fun trying to make the bash programm as useful as possible. Now the string is passed to the Bash script using the print function, which in his turn gives it to the **Search_plot.py**.
<br/> <br/> 
<span style="color: #dc143c;">*PS: if the file has more than two columns the user should put which columns he'd like to choose !*</span>

 <span style="color: #ffd33d; font-weight: bold;">&emsp;&#8226; Search_plot.py</span>
 
&emsp;Since the data is passed as a string here, the dictionnaries must be built here. And using the boundary values, it searchs if the given interval corresponds to one of the existing intervals, or else it searches in which existing intervals belong the valeues and then it takes both of them and plots. To make good scientific stuff the user should use a small step ( I recommand 1), thus the programm can collect the exat data.

##  <span style="color: #2ecc71;"> How to tweak this project for your own uses !

&emsp;You may notice that this project is made in some indisipline and wierd way, but there are some restrictions, because it's a school project, and the aim here is to focus on some modules and not use all existing modules. However, I think there can be some tricks that can be useful to some other project. <br/>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**SO feel free to copy and use it**

## <span style="color: #2ecc71;"> Find a bug?

&emsp;If you found an issue or would like to submit an improvement to this project or any kind of idea, please submit an issue using the issues tab above. 


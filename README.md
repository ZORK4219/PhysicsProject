 
# Search and Plot Physics dataFile 

## A Python-Bash project searching in file and plotting data using matplotlib

This is a school project, that was built for instance to process a txt file containing data about wavelength and intensities, and take out important data to be able to plot it. Every part of this project contains three sample codes which shows how to do the following:

- Using a terminal, a command should excute the Bash program, with adding parameters which are explained using -help.
- The Bash program then verifies if the parameters correspond to the rules(which I impose to stay in context of the physics we're dealing with).

- Then the **Intensity.py** Python programm is called with the given parameters, it searches the file, take out the important data, which in my case was wavelength and light intensities. Then it builts a Python dictionary, for each one of the quantities, and it must return it using print function to Bash programm.

The details about each program will be breifly explained in the next section, and the scripts have already some comments that can guide the user.

## How  does each programm work?

I will give you here a breif idea, in the simplest way possible to see how each one works :

###   \- *Bash script*
 &emsp;&emsp; It start by looking if the user, put -help command, if he did, it dispalys help, or else it starts examining all the parameters to see if they are acceptable or else it exists the programm. If everything is good, it asks for boundary values to plot the interval. It calls **Intensity.py** and store the result in a variable then pass it to **Search.py** and then the programm takes care of the rest and plots the data.

###  \- *Python scripts*
- **Intensity.py**<br/> 
&emsp;This program searches for the file indicated in the parameters then it starts looking in it using **re** module, we take the data, and then we build to dictionnaries, one for wavelength the other for intensities, where the values are split by a step of integer passed as parameter. Here I used some kind of wierd way to pass the dictionnary to the other programm, because I wanted to make the Bash programm useful, but there are many easy ways to do it. So here creat a sting and put all the data in it and then return it to the Bash script using the print function. Now as explinained above it passes it to the **Search_plot.py**.

- **Search_plot.py** <br/> 
&emsp;Since the data is passed as a string here, it rebuilds the dictionary again. And using the boundaries values, it searchs if the given interval corresponds to one of the existing intervals, or else it searches in which existing intervals belong the valeues and then it takes both of them and plots.

## How to tweak this project for your own uses

&emsp;You may notice that this project is made in some indisipline and wierd way, but there are some restrictions, because it's a school project, and the aim here is to focus on some modules and not use all existing modules. However, I think there can be some tricks that can be useful to some other project. <br/>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**SO feel free to copy and use it**

## Find a bug?

&emsp;If you found an issue or would like to submit an improvement to this project or any kind of idea, please submit an issue using the issues tab above. 


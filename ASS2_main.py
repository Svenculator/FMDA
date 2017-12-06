# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:17:41 2017

@author: Sven
This is where the magic happens
"""
#%%
import os
os.chdir('D:\\Dropbox\\Universiteit\\FMDA') # Set working directory
import ASS2_function as fn


#%% Set the working directory to what you want it to be

#os.chdir('D:\\Dropbox\\Universiteit\\FMDA') # Set working directory
#print('Working directory is:', os.getcwd())

#%%
#zoeken naar 0 om te weten of er geen data mist en uitleggen waarom de data mist. Bijv fishiries in een land waar geen water is.

SI = fn.GHGcountry('SI') #This will put all the data of Slovenia in a variable
print(SI[:50]) #Looks like there are a lott of zeroes so a lott of missing data

newSI= fn.filterzero(SI) #Filter out all non data 

#%% Benford formula

#Benford's law in Python.


import re
import matplotlib.pyplot as plot

from math import log10

def plot_benford(iterable):
    #Plot leading digit distribution in a string iterable.

    numbers = [float(n) for n in range(1, 10)]

    # Plot the frequencies as predicted by the law.
    benford = [log10(1 + 1 / d) for d in numbers]
    plot.plot(numbers, benford, 'ro', label = "Predicted")

    # Plot the actual digit frequencies.
    data = list(digits(iterable))
    plot.hist(data, range(1, 11), align = 'left', normed = True,
              rwidth = 0.7, label = "Actual")

    # Set plot parameters and show it in a window.
    plot.title("Benford's Law")
    plot.xlabel("Digit")
    plot.ylabel("Frequency")

    plot.xlim(0, 10)
    plot.xticks(numbers)
    plot.legend()

    plot.show()

def digits(iterable):
    """Yield leading digits of number-like strings in an iterable.
    """

    numexp = re.compile(r'\d+(\.\d+)?([eE]\d+)?')
    leading = set("123456789")

    for item in iterable:
        for match in numexp.finditer(str(item)):
            for digit in match.group(0):
                if digit in leading:
                    yield int(digit)
                    break
                


#if _name_ == "_main_":
#    import fileinput
#    import random
#    my_randoms = random.sample(range(1000), 1000)
#    plot_benford(my_randoms)
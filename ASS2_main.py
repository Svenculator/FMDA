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
print(newSI[:50]) #Zeroes are gone! 

newerSI=fn.beginzero(newSI)

#%%
#sven=fn.digits(newSI)
#print(sven)
#fn.plot_benford(newSI)

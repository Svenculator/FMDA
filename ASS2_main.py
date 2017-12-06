# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:17:41 2017

@author: Sven
This is where the magic happens
"""
#%%
import os
import ASS2_function as fn


#%% Set the working directory to what you want it to be

os.chdir('D:\\Dropbox\\Universiteit\\FMDA') # Set working directory
print('Working directory is:', os.getcwd())

#%%
#zoeken naar 0 om te weten of er geen data mist en uitleggen waarom de data mist. Bijv fishiries in een land waar geen water is.

SI = fn.GHGcountry('SI')

#%%

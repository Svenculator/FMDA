# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:29:19 2017

@author: Sven van Baren 
Assignment 2 FMDA
"""
#%%
import os
import csv
import re
import matplotlib.pyplot as plot
from math import log10
#%% Set the working directory to what you want it to be

os.chdir('D:\\Dropbox\\Universiteit\\FMDA') # Set working directory
#print('Working directory is:', os.getcwd())

#%%

def GHG(countrycode, year, pollutant, sectorcode): #With this function you can call any emmission of any country/sector/pollutant
    try:
        with open('UNFCCC_v20.csv', 'r') as GHG_EU:
            readGHG = csv.reader(GHG_EU, delimiter = '\t')
            header=next(readGHG, None) #Skip header
            countriesdata=dict()
            sectorsdata=dict()
            main_data= dict()
            main_data={'countrycode': [], 
                       'formatname' : [], 
                       'polname': [], 
                       'year' : [],
                       'sectorname': [],
                       'parentsectorcode': [],
                       'sectorcode': [],
                       'notation' : [],
                       'unit': [],
                       'emissions': [],
                       'datasource' : [],
                       'publicationdate' :[]}  
            for row in readGHG:
                countryc= str(row[0])
                countriesdata[countryc]= row[1]
                sector = str(row[7])
                sectorsdata[sector]=row[5], row[6]
                
                main_data['countrycode'].append(row[0])
                main_data['polname'].append(row[3])
                main_data['year'].append(row[4])
                main_data['unit'].append(row[9])
                main_data['emissions'].append(row[10])
                main_data['sectorcode'].append(row[7])
                main_data['parentsectorcode'].append(row[6])
                
                        
            for x in range (len(main_data['countrycode'])):
                if main_data['countrycode'][x] == countrycode:
                    if main_data['year'][x] == year:
                        if main_data['polname'][x]== pollutant:
                            if main_data['sectorcode'][x] == sectorcode:
                                print('In',countriesdata[countrycode],'the emission of',pollutant,'in',year,
                                      'in sector',sectorsdata[sectorcode],'are', main_data['emissions'][x],main_data['unit'][x])
                            
    except: 
        print("ERROR, something went wrong.\nType in all variables of the function as strings. It is also possible that the combination of variables doesn't exist for this country")
     
 
#%% Nu alles van een heel land

def GHGcountry(countrycode):
    try:
        with open('UNFCCC_v20.csv', 'r') as GHG_EU:
            readGHG = csv.reader(GHG_EU, delimiter = '\t')
            header=next(readGHG, None) #Skip header
            countriesdata=dict()
            sectorsdata=dict()
            main_data= dict()
            list_parentseccode=[]
            datacountry=[]
            main_data={'countrycode': [], 
                       'formatname' : [], 
                       'polname': [], 
                       'year' : [],
                       'sectorname': [],
                       'parentsectorcode': [],
                       'sectorcode': [],
                       'notation' : [],
                       'unit': [],
                       'emissions': [],
                       'datasource' : [],
                       'publicationdate' :[]}  
            for row in readGHG:
                countryc= str(row[0])
                countriesdata[countryc]= row[1]
                sector = str(row[7])
                sectorsdata[sector]=row[5], row[6]
                
                #make list of parent sectors only once
                if row[6] not in list_parentseccode:
                    list_parentseccode.append(row[6])
                
                main_data['countrycode'].append(row[0])
                main_data['polname'].append(row[3])
                main_data['year'].append(row[4])
                main_data['unit'].append(row[9])
                main_data['emissions'].append(row[10])
                main_data['sectorcode'].append(row[7])
                main_data['parentsectorcode'].append(row[6])
                
                        
            for x in range (len(main_data['countrycode'])):
                if main_data['countrycode'][x] == countrycode:
                    if main_data['sectorcode'][x] not in list_parentseccode:
                        datacountry.append(float(main_data['emissions'][x]))
            return datacountry
    except:
        print('Only enter countrycodes which exist in the database as strings')
        
#%%SANITY Check --> eerst tellen hoeveel nullen in het bestand
#--> dan sectorname aan deze nullen toewijzen --> misschien doet land niets in sector

#def missing_data(country):
with open('UNFCCC_v20.csv', 'r') as GHG_EU:
        readGHG = csv.reader(GHG_EU, delimiter = '\t')
        header=next(readGHG, None) #Skip header
        countriesdata=dict()
        sectorsdata=dict()
        main_data= dict()
        list_parentseccode=[]
        main_data={'countrycode': [], 
                   'formatname' : [], 
                   'polname': [], 
                   'year' : [],
                   'sectorname': [],
                   'parentsectorcode': [],
                   'sectorcode': [],
                   'notation' : [],
                   'unit': [],
                   'emissions': [],
                   'datasource' : [],
                   'publicationdate' :[]}  
        for row in readGHG:
            countryc= str(row[0])
            countriesdata[countryc]= row[1]
            sector = str(row[7])
            sectorsdata[sector]=row[5], row[6]
            
            #make list of parent sectors only once
            if row[6] not in list_parentseccode:
                list_parentseccode.append(row[6])
            
            main_data['countrycode'].append(row[0])
            main_data['polname'].append(row[3])
            main_data['year'].append(row[4])
            main_data['sectorname'].append(row[5])
            main_data['unit'].append(row[9])
            main_data['emissions'].append(row[10])
            main_data['sectorcode'].append(row[7])
            main_data['parentsectorcode'].append(row[6])
            
        nodata_sec=dict()
        
        for data in range (len(main_data['countrycode'])):
            if main_data['countrycode'][data] == 'SI':
                if float(main_data['emissions'][data]) == 0:
                    sec = main_data['sectorcode'][data]
                    
        


                    
                
            
            
            
            
            
    
#        count_mis = 0
#        count_hit = 0
#        sector_mis = []
#        sector_hit = []
#        for data in range(len(main_data['emissions'])):
#            if (main_data['countrycode'][data]== country) or (main_data['country'][data]== country):
#                if float(main_data['emissions'][data]) == 0:
#                    count_mis = count_mis + 1
#                    sector_mis.append(main_data['sectorname'][data])
#                else:
#                    count_hit = count_hit + 1
#                    sector_hit.append(main_data['sectorname'][data])
#                
#    return sector_mis, count_mis, sector_hit,count_hit
            


#%%
def filterzero(file): #function to filter out all the zeroes of the data, so where no data is available
    list_nozero=[]
    for line in file:
        if line >0:
            list_nozero.append(line)
    return list_nozero

#%% Benford formula

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


# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:29:19 2017

@author: Sven van Baren 
Assignment 2 FMDA
"""
#%%
import os
import csv

#%% Set the working directory to what you want it to be

os.chdir('D:\\Dropbox\\Universiteit\\FMDA') # Set working directory
print('Working directory is:', os.getcwd())

#%%

def GHG(countrycode, year, pollutant, sectorcode): #With this function you can call any emmission of any country/sector/pollutant
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
                            
        
GHG('AT', '1992', 'CH4','1.A.1')
        
#zoeken naar 0 om te weten of er geen data mist en uitleggen waarom de data mist. Bijv fishiries in een land waar geen water is.
        
#%% Nu alles van een heel land

#def GHG(countrycode, year, pollutant, sectorcode): #With this function you can call any emmission of any country/sector/pollutant

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


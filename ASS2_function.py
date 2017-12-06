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
                        float(datacountry.append(main_data['emissions'][x]))
            return datacountry
    except:
        print('Only enter countrycodes which exist in the database as strings')


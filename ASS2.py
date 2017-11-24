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
try: #Misschien ook with gebruiken op het laatste als ik tijd over heb en functie van maken
    GHG_EU = open('UNFCCC_v20.csv', 'r') #open file
    print(GHG_EU)
except: 
    print('Open failed')    #Build in fail safe

head = GHG_EU.readline()

print(head)

#%%
with open('UNFCCC_v20.csv', 'r') as GHG_EU:
    readGHG = csv.reader(GHG_EU, delimiter = '\t')
    header=next(readGHG, None) #Skip header
    list_CC=[]
    list_CN=[]
    list_FN=[]
    list_PN=[]
    list_Y=[]
    list_SN=[]
    list_PSC=[]
    list_SC=[]
    list_N=[]
    list_U=[]
    list_E=[]
    list_DS=[]
    list_PD=[]
    for row in readGHG:
        CC= row[0]
        CN= row[1]
        FN= row[2]
        PN= row[3]
        Y= row[4]
        SN= row[5]
        PSC= row[6]
        SC= row[7]
        N= row[8]
        U= row[9]
        E= row[10]
        DS= row[11]
        PD= row[12]
        
        list_CC.append(CC)
        list_CN.append(CN)
        list_FN.append(FN)
        list_PN.append(PN)
        list_Y.append(Y)
        list_SN.append(SN)
        list_PSC.append(PSC)
        list_SC.append(SC)
        list_N.append(N)
        list_U.append(U)
        list_E.append(E)
        list_DS.append(DS)
        list_PD.append(PD)
        
#mytuple = tuple(mylist) #To make it a tuple
      
print(list_CC[0:100])        


#%%

list_CC=[]
list_CN=[]
list_FN=[]
list_PN=[]
list_Y=[]
list_SN=[]
list_PSC=[]
list_SC=[]
list_N=[]
list_U=[]
list_E=[]
list_DS=[]
list_PD=[]
for line in GHG_EU:
    CC, CN, FN, PN, Y, SN, PSC, SC, N, U, E, DS, PD = line.split('\t')
    list_CC.append(CC)
    list_CC.append(CN)
    list_CC.append(FN)
    list_CC.append(PN)
    list_CC.append(Y)
    list_CC.append(SN)
    list_CC.append(PSC)
    list_CC.append(SC)
    list_CC.append(N)
    list_CC.append(U)
    list_CC.append(E)
    list_CC.append(DS)
    list_CC.append(PD)
    
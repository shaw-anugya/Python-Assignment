#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def graph(cars, columns = None, directory = None, graph_type = None):

    import numpy as np   #importing the necessary libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os

    sns.set() 
    
    if directory is None:
           directory=os.getcwd() #current working directory is stored
        
    if columns is None:
        columns = list(df.columns)
   
    #taking empty list for categorical and numerical types
    categorical=[]
    numerical=[]   
    
    #if value of graph_type is hist
    if graph_type == 'Hist':
        
        #check for numerical variable
        for i in columns:
            if((np.dtype(df[i])=='float') or (np.dtype(df[i])=='int')):
                numerical.append(i)
            else:
                print('{} is not numerical,so Histogram cannot be plotted.'.format(i))
                
        #if list is not empty,then print the column   
        if numerical != []:
            print('Numerical columns are',numerical)
    
        for i in numerical:
            #plotting histogram
            df.hist(column=i,grid= False, figsize=(6,4))
            plt.xlabel(i,fontsize=15)
            plt.ylabel('Number of elements',fontsize=12)
            plt.title('Histogram of '+i.upper(),fontsize=15)
            plt.savefig(directory+"/Histogram of "+i+".png")
            plt.show()
        
    
    #if value of graph_type is box
    elif graph_type == 'Box':
        
        #check for numerical variable
        for i in columns:
            if((np.dtype(df[i])=='float') or (np.dtype(df[i])=='int')):
                numerical.append(i)
            else:
                print('{} is not numerical,so Boxplot cannot be plotted.'.format(i))    
        #if list is not empty         
        if numerical != []:
            print('Numerical columns are',numerical)
       
    
        for i in numerical:
            #plotting boxplot
            df.boxplot(column=i,fontsize=15)
            plt.ylabel('Number of elements',fontsize=12)
            plt.title('Boxplot of '+i.upper(),fontsize=15)
            plt.savefig(directory+"\\Boxplot of "+i+".png")
            plt.show()
                
                
    #if value of graph_type is box            
    elif graph_type == 'Barh':
       
        #check for categorical variable
        for i in columns:
            if (np.dtype(df[i])=='object'or len(np.unique(df[i]))<15):
                categorical.append(i)
            else:
                print('{} is not categorical,so Bargraph cannot be plotted.'.format(i))   
        #if list is not empty         
        if categorical != []:
            print('Categorical columns are',categorical)
    
        for i in categorical:
            #plotting of bar graph
            df[i].value_counts().plot(kind='barh',color='green',fontsize=15)
            plt.xlabel('Number of Elements',fontsize=15)
            plt.ylabel(i,fontsize=15)
            plt.title('Bargraph of '+i,fontsize=15)
            plt.savefig(directory+"/Bargraph of "+i+".png")
            plt.show()
            
    elif graph_type == 'All':
        for i in columns:
            if (np.dtype(df[i])=='object'or len(np.unique(df[i]))<15):
                categorical.append(i)
            else :
                numerical.append(i)
        print('Categorical columns are',categorical)
        print('Numerical columns are',numerical)
        
        for i in categorical:
            df[i].value_counts().plot(kind='barh',color='green',fontsize=15)
            plt.xlabel('Number of Elements',fontsize=15)
            plt.ylabel(i,fontsize=15)
            plt.title('Bargraph of '+i,fontsize=15)
            plt.savefig(directory+"/Bargraph of "+i+".png")
            plt.show()

        for i in numerical:
            #plotting histogram
            df.hist(column=i,grid= False, figsize=(6,4))
            plt.xlabel(i,fontsize=15)
            plt.ylabel('Number of elements',fontsize=12)
            plt.title('Histogram of '+i.upper(),fontsize=15)
            plt.savefig(directory+"/Histogram of "+i+".png")
            plt.show()

            #plotting boxplot
            df.boxplot(column=i,fontsize=15)
            plt.ylabel('Number of elements',fontsize=12)
            plt.title('Boxplot of '+i.upper(),fontsize=15)
            plt.savefig(directory+"\\Boxplot of "+i+".png")
            plt.show()

            


#!/usr/bin/env python
# coding: utf-8

# In[3]:


#creating a packagae

class graphical:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    import tkinter as tk
   
    from tkinter import filedialog

    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
    canvas1.pack()

    def getCSV ():
        global df
    
        import_file_path = filedialog.askopenfilename()
        df = pd.read_csv (import_file_path)
        print (df)
    
    browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_CSV)

    root.mainloop()
    def graphs(df,l=None, directory):
        
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import os
        if directory is None:
            directory=os.getcwd() #current working directory is stored
        
        
        if l:
            count=1
            d={}  
            name=[] #creating a list with inputed column names
            for i in df:
                d[count]=i
                count+=1
            for i in l:
                name.append(d[i])
            #separating the categorical and numerical data
            categorical=[]
            numerical=[]


            for i in name:
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
                plt.title('Bargraph of'+i,fontsize=15)
                plt.savefig(directory+"Bargraph of "+i+".png")
                plt.show()

            for i in numerical:
                #plotting histogram
                df.hist(column=i,grid= False, figsize=(6,4))
                plt.xlabel(i,fontsize=15)
                plt.ylabel('Number of elements',fontsize=12)
                plt.title('Histogram of'+i.upper(),fontsize=15)
                plt.savefig(directory+"/Histogram of "+i+".png")
                plt.show()
               #plotting boxpplot
                df.boxplot(column=i,fontsize=15)
                plt.ylabel('Number of elements',fontsize=12)
                plt.title('Boxplot of'+i.upper(),fontsize=15)
                #plt.savefig(directory+"\\Boxplot of "+i+".png")
                plt.show()
              
        elif(l==[]):
            print('Enter the columns you want to plot the graph')
        elif (l==None):
            return (graph1(df)) 


# In[ ]:


# download as .py # create new text doc with the name __init__py
 


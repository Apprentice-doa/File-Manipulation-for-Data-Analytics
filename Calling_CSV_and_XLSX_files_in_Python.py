#Importing the required libraries

import pandas as pd
import openpyxl
from csv import reader
from pandas import DataFrame

# Expands the dataframe without limitations
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Code block for calling excel files
#E_File = pd.read_excel(r"C:\Users\danie\OneDrive\Documents\iris data.xlsx")print(E_File)

file = pd.read_csv(r"C:\Users\danie\OneDrive\Desktop\Data Sets\iris data.csv") # Read the csv into the IDE
filed = DataFrame(file,
                   columns=['Observation', 'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']) #Convert the file into a dataframe
print(filed)

strfile = str(filed) # Make the dataset all strings
print(strfile)

note = open("C:\\Users\\danie\\OneDrive\\Desktop\\Data Sets\\Aproko.doc", 'w')  # Using 'a' instead of 'w' does not override the content, but appends it
note.write(strfile)
note.close()

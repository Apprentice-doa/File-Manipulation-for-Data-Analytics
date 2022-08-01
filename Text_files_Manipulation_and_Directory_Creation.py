#Importing the required libraries
import os
from os import rename
from os import remove
from os import mkdir

invent = os.path.join("C:\\", "Users\\", "danie\\", "PycharmProjects\\", "Python_Format_Files") # Creating a Directory
if not os.path.exists(invent):
    os.mkdir(invent)

# Removing and renaming files on your drive, server of computer
# remove("C:\\Users\\danie\\PycharmProjects\\Python_Format_Files\\Apprentice.txt")
# rename("C:\\Users\\danie\\PycharmProjects\\Python_Format_Files\\Apprentice.txt", "C:\\Users\\danie\\PycharmProjects\\Python_Format_Files\\Aproko.txt") // You can also change the extension using rename.

#Create and write into a text file
note = open("C:\\Users\\danie\\OneDrive\\Desktop\\Data Sets\\Aproko.txt", 'w') # 'w' = write
note.write("\nTaking territories")
note.write("\nI am in the temple")
note.close()

#Read a text file line by line
alvaro = open("C:\\Users\\danie\\OneDrive\\Desktop\\Data Sets\\Aproko.txt", 'r') # 'r' = read
for line in alvaro:
    print(line, end='')
alvaro.close()

#Create and write into a doc file
note = open("C:\\Users\\danie\\OneDrive\\Desktop\\Data Sets\\Aproko.doc", 'w')
note.write("\nTaking territories")
note.write("\nI am in the temple")
note.close()

#Read a doc file line by line
alvaro = open("C:\\Users\\danie\\OneDrive\\Desktop\\Data Sets\\Aproko.doc", 'r')
for line in alvaro:
    print(line, end='')
alvaro.close()


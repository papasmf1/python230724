import pandas as pd 
import re 

origin = open("temp.csv")
myCopy = open("temp_copy.csv", "wt")
line = origin.readline() 
while (line != ''):
    if re.search('rep', line):
        line = origin.readline()
    myCopy.write(line)
    line = origin.readline() 
    

origin.close()
myCopy.close() 


df = pd.read_csv("temp_copy.csv", 
    sep="\s+", 
    header=None,
    names=["1열","2열","3열","4열","5열"])
#print(df.info())
print(df["1열"].sum())
print(df["1열"].mean())
print(df["1열"].count())

#print(df)
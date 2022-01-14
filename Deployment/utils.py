import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import os

pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)


# path = "/home/sebastian/walmartDigital/de-challenge/data";

parentPath = "../data";
#read a csv file from the path obtained by concatenate parentPath and filename
#return pandas dataframe object
def readCsv(filename):
    df = pd.read_csv(parentPath+"/"+filename,sep=',',encoding='ISO-8859-1')
    return df

#get List of df from a path. 
#return list of dataframes
def getDfList():
    filenameList = os.listdir(parentPath)
    dfList = list()
    for filename in filenameList:
        dfList.append(readCsv(filename))
    return dfList

#join 2 dataFrames by a column 
#return a new pandas dataframe with the union of df1 and df2
def joinByColumn(df1,df2,columnName):
    return df1.merge(df2, left_on=columnName, right_on=columnName)
    # return df1.join(df2.set_index(columnName), on=columnName)

#join 2 dfs by a columnName (in this case its a constant = "console")
#return the union of 2 df in pandas object
def joinList():
    columnName = "console"
    dfList = getDfList()
    df1 = dfList[0].head(10)
    df2 = dfList[1].head(10)

    print(df1)
    print(df2.columns)
    # return joinByColumn(df1,df2,columnName)
    
joinList = joinList()

print(joinList)





# df1.set_index('key').join(other.set_index('key'))




# def readCsv():
#     df  = pd.read_csv("../data ")


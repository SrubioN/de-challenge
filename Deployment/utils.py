import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import pandas as pd 
import numpy as np 
import os

pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.options.mode.chained_assignment = None 
parentPath = "../data"

#read a csv file from the path obtained by concatenate parentPath and filename
#return pandas dataframe object
def readCsv(filename):
    df = pd.read_csv(parentPath+"/"+filename,sep=',',encoding='ISO-8859-1')
    return df

#get List of df from a path. 
#return list of df
def getDfList():
    filenameList = os.listdir(parentPath)
    dfList = list()
    for filename in filenameList:
        dfList.append(readCsv(filename))
    return dfList


def stripDf(df):
    for col in df.columns:
        # print(df[col].dtypes!='int64')
        if(df[col].dtypes!='int64'):
            df[col] = df[col].str.strip()
    return df

dfList = getDfList()
df1 = stripDf(dfList[0])
df2 = stripDf(dfList[1])


# df1 = dfList[0].head(1000)
# df2 = dfList[1]   

# #use strip() function to remove leading and trailing whitespaces.
# df1.console=df1.console.str.strip() 
# df2.console=df2.console.str.strip() 
# df2.company=df2.company.str.strip() 



data = df2.set_index('console')


def mapCompanyByConsole(row):
    return data.loc[[row.console]].values[0] 

# print(df1.company)
df1['company'] = df1.apply(mapCompanyByConsole, axis=1)
df1.name = df1.name.str.strip()


# print(df1.shape)
# df1.drop_duplicates('name', keep='first')
# print(df1.shape)

# print(df1.columns)




# print(df1.groupby(["name","console"])[["metascore"]].sum())

# print(df1.groupby(["name"])[["metascore"]].sum())

def continueStatistics(groupClause,var,data):
  df = pd.DataFrame()
  df['min'] = data.groupby(groupClause)[var].min()
  df['max'] = data.groupby(groupClause)[var].max()
  df['count'] = data.groupby(groupClause)[var].count()
  df['mean'] = data.groupby(groupClause)[var].mean()
  df['median'] = data.groupby(groupClause)[var].median()
  df['std'] = data.groupby(groupClause)[var].std()
  return df
# print(df1.columns)
# data = data.groupby(['Region','Patologia'])[['Region','Patologia','Counts']].count()


statistics = continueStatistics(['console','name'],'metascore',df1)
treshold= 10
# print(statistics)

# def pieChartValorationPerConsole():
    


consoles = np.array(df2.console)
# df2.company = df2.companies.str.strip()
companies = np.array(df2.drop_duplicates('company', keep='first').company)

pieChartValues = []
# prom = df1.groupby(["console","name"])['metascore'].sum()/df1.groupby(["console","name"])['metascore'].count()
df1.groupby(["console","name"]).agg({'metascore':np.mean})


minimun  = df1.metascore.min()
maximun = df1.metascore.max()

ax = df1.pivot(index='console',columns='name',values='metascore').plot(kind='bar')
legend = ax.legend(loc="upper left", bbox_to_anchor=(1.02, 0, 0.07, 1))

# pixels to scroll per mousewheel event
d = {"down" : 30, "up" : -30}
# fig, ax = plt.subplots()


def func(evt):
    if legend.contains(evt):
        bbox = legend.get_bbox_to_anchor()
        bbox = Bbox.from_bounds(bbox.x0, bbox.y0+d[evt.button], bbox.width, bbox.height)
        tr = legend.axes.transAxes.inverted()
        legend.set_bbox_to_anchor(bbox.transformed(tr))
        ax.get_figure().canvas.draw_idle()

ax.get_figure().canvas.mpl_connect("scroll_event", func)
# plt.show()
    # prom.plot.bar(rot=0)
    # plt.show()
    # print(df1[["console","name","metascore"]])

    # print(consoles[0])

    # print(df1.console)
    
    
    # i = 0
    # for console in consoles:
    #     aux = df1.loc[df1['console']==console].sort_values("metascore", ascending=False).head(treshold)
        
    #     aux.metascore.max()

    #     minimum = aux.metascore.min()-5
    #     maximum = aux.metascore.max()+5


    #     # aux["metascore"] =  aux["metascore"]/aux.metascore.max()
    #     # print()
    #     # if(i==0):
    #     plt.subplot()
    #     ax = aux[["name","metascore"]].plot.bar(x="name",y="metascore")
    #     ax.set_ylim([minimum,maximum])
    #     plt.show()
        # break
    
    # print(df1[consoles[0]])
    # prom["metascore"].
    # topData = pd.DataFrame()
    # i = 0
    # for console in consoles:
    #     games = prom[console].index
    #     for game in games:
    #         topData[game]=
    
    # suma["X360"]["Diablo III"]

    # print(suma.sort_values("metascore"))
    # print()
    # data = df2.loc[["company"]==consoles[0]]
    # companies = df2.company
    # print(consoles[0])
    
    # print(companies)
    # consoles = np.array()


# pieChartValorationPerConsole()
    

# def joinList():
#     columnName = "console"
#     

#     print(df1)
#     print(df2.columns)
#     # return joinByColumn(df1,df2,columnName)







# df1.set_index('key').join(other.set_index('key'))




# def readCsv():
#     df  = pd.read_csv("../data ")


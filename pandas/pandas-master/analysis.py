
import pandas as pd

df = pd.read_csv("C:\Sandbox\my-dev-repo\pandas\pandas-master\pokemon_data.csv")

#print(poke.tail(5))

#print(type(df))

#print(df.head(5))

#print(df.columns)


#print(df[['Name']])
#print(df.Name)
#print(df[['Name', 'HP']])

#integer location
    #selecting rows (for all columns)
    #print(df.iloc[0:2])

    #selecting exact location (R, C) - lists are exclusive
    #print(df.iloc[:5,0:1])

df2 = df.head(5)

for rownum, row in df2.iterrows():
    #print("type of index: " , type(index))
    #print("type of row: " , type(row))
    if (rownum == 0):
        #print(index, row['Name'])
        for i in row.values:
            print(i)
        print(row.values)
        #print(row.array)
        #print(row.__array__)

#series.array - return values
#series.values
#series.index - returns column names
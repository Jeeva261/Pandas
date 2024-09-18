# Load a CSV file into a Pandas DataFrame.
import pandas as pd

x=pd.read_csv("dirtydata.csv")
print(x.to_string())

# Perform basic data manipulations like filtering, sorting, and grouping
student={
    "name":["A","B","A","B","C"],
    "age":[20,50,40,30,60],
    "score":[95,60,45,100,101]

}

# filtering,sorting,grouping

data=pd.DataFrame(student)
new_filter=data[data["age"]>50]
print(new_filter)

data=pd.DataFrame(student)
sorted=data.sort_values("age")
print(sorted)

data=pd.DataFrame(student)
group=data.groupby("name")["score"].max()
print(group)

egg=data.groupby("name").agg({
    "score":["max","min","mean"]
})
print(egg)

# Load a dataset with missing values and handle them using different techniques
# Write a script to replace missing values with the mean of the column
import pandas as pd

df=pd.read_csv("dirtydata.csv")
df.dropna(inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df.fillna(3000000,inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
res=df.info()
print(res)

df=pd.read_csv("dirtydata.csv")
df["Calories"].fillna(df["Calories"].mode()[0],inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df["Date"]=pd.to_datetime(df["Date"])
df.dropna(subset="Date",inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df.loc[7,"Duration"]=120
print(df)


df=pd.read_csv("dirtydata.csv")
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i,"Duration"]=130

print(df)

df=pd.read_csv("dirtydata.csv")
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
res=df.duplicated()
print(res)

df=pd.read_csv("dirtydata.csv")
res=df.drop_duplicates()
print(res)
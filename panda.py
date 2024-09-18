import pandas as pd 

# Dataframe
data={
    "Name":["jeeva","sanjay","vijay","yogesh","madhan","dhanush"],
    "Age":[20,30,40,50,60,20],
    "class":[1,2,3,4,5,6]
}

df=pd.DataFrame(data,["one","Two","three","four","five","sex"])
print(df.loc["one"])

# series

x=[1,2,3,4,5,6]
df=pd.Series(x,["one","Two","three","four","five","sex"])
print(df.loc["one"])


car={
    "apple":25,
    "orange":30,
    "banana":40
}

df=pd.Series(car,["apple"])
print(df.loc["apple"])


# read csv file and json file

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Pandas\file.csv'
df=pd.read_csv(file_path)
print(df)

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Pandas\file.json'
df=pd.read_json(file_path)
print(df)

# Analyze data

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Pandas\file.csv'
df=pd.read_csv(file_path)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.columns)
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.nunique())
print(df.duplicated().sum())


# data cleaning
# fillna

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df=df.fillna(1300)
print(df)

# fillna with mean median mode

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Calories"].fillna(df["Calories"].mean(),inplace=True)
print(df)

df=pd.read_csv(file_path)
df["Calories"].fillna(df["Calories"].median(),inplace=True)
print(df)

df=pd.read_csv(file_path)
df["Calories"].fillna(df["Calories"].mode()[0],inplace=True)
print(df)

# dropna

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.dropna(inplace=True)
print(df)

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.dropna(subset="Calories",inplace=True)
df.drop("Duration", axis=1, inplace=True)
print(df)


# data format


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Date"]=pd.to_datetime(df["Date"])
print(df)


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Date"]=pd.to_datetime(df["Date"])
df.dropna(subset="Date",inplace=True)
print(df)


# worng data

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.loc[7,"Duration"]=10000
print(df)


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i]=1000
print(df)


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)
print(df)


# remove duplicates

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.drop_duplicates(inplace=True)
print(df)

# replace

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Duration"]=df["Duration"].replace(60,1200)
print(df)

# corr

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file1.csv'
df=pd.read_csv(file_path)
print(df.corr())

# save files

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file1.csv'
df=pd.read_csv(file_path)
df.to_csv("demo.csv")






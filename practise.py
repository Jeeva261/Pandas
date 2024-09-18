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
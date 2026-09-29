import pandas as pd
 
data = {
    "name": ["A", "B", "C",'D','E','F','G'],
    "marks": [85, 90, 78,66,32,82,None]                     #use None for null values in pandas
}
 
df = pd.DataFrame(data)


#head()

print(df.head())          
#It shows the first 5 rows
print(df.head(7))
#It shows the first 7 rows

#tail()
print(df.tail())
#Its similar to head just it shows last 5 rows



# info()

print(df.info())  
#It shows the summary i.e totalrows,columns,columnsnames,data types,null values.


# describe()

print(df.describe())
#It shows the statistics summary of the data i.e count mean,min,max,etc.



# Rows and Index
# Each row has an index. By default, it is just a number.

# The index helps Pandas:

# align data
# keep rows connected across operations
# You usually do not need to change it early on.



# Commonly Used Pandas Functions

# Purpose	              Function

# View first rows	       head()
# Dataset summary	       info()
# Statistical summary	   describe()
# Select column	           df["col"]
# Filter rows	           df[condition]
# Check missing values	   isna()
# Remove missing values	   dropna()
# Fill missing values	   fillna()
# Rename columns	       rename()
# Change data type	       astype()
# Remove duplicates	       drop_duplicates()
# String operations	       str.lower(), str.strip()
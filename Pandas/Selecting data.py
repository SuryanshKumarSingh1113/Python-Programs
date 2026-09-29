import pandas as pd

df=pd.DataFrame({
    'Product name':["Iphone","Samsung","Redmi","Nokia","Moto",None] *200,
    'Price':[2000,1500,400,900,10,20]*200,
    "Storage":[256,256,64,124,50,None]*200,
    "Rating":[5,5,4,3,2,0]*200

})

# Selecting Data

# Select single column:
print(df["Price"])

# Select multiple columns:
print(df[["Product name","Storage","Price"]])

# This column-based thinking is central to Pandas.


# Selecting Rows with Conditions

  #Filter rows using conditions
print(df[df["Price"] > 1000])

  #Multiple conditions:
print(df[(df["Price"]>800) &(df["Rating"]>4)])


# Handling Missing Values

# Check missing data:
print(df.isna())
print(df.isna().sum())

# Remove missing values:
print(df.dropna())
print(df.isna().sum())

# Fill missing values:
df["Storage"] = df["Storage"].fillna(df["Storage"].mean())


# Changing Data Types
# Check data types:

print(df.dtypes)

# Convert types:

df["Price"] = df["Price"].astype(float)

# Incorrect data types lead to incorrect analysis.


#check duplicates
print(df.duplicated().sum())

# Removing Duplicates
print(df.drop_duplicates())
#Duplicates silently distort results if not handled.


# Basic String Cleaning

df["Product name"] = df["Product name"].str.upper()
print(df.head())
df["Product name"] = df["Product name"].str.strip()
# String cleaning is common in real-world datasets.


# Renaming Columns
df = df.rename(columns={"Product name": "product_name"})
print(df.dtypes)
# Clean column names make code readable and consistent.


# Renaming Columns
# Clean column names early:

df = df.rename(columns={"Product name": "product_name"})

# Clean column names make code readable and consistent.


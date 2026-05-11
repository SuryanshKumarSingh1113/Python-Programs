# From a dictionary:

import pandas as pd
 
data = {
    "name": ["A", "B", "C",'D','E','F','G'],
    "marks": [85, 90, 78,66,32,82,None]                     #use None for null values in pandas
}
 
df = pd.DataFrame(data)
print(df)

# Each key becomes a column.




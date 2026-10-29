import pandas as pd 

data = {
    "Name": ["Alice","Bob","Charlie"],
    "Age": [25,30,35],
    "City": ["New York","San Fransico","Los Angles"]
}

df = pd.DataFrame(data)
print(df)
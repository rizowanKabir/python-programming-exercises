import pandas as pd 

data = {
    "Product": ["Pen","Book","Bag","Pencil","Books"],
    "Sales": [100,500,900,150,300]
}

df = pd.DataFrame(data)

print(df)
print(df[df["Sales"] > 200])
print(df[df["Product"] == "Pen"])
print(df.sort_values(by="Sales",ascending=True))
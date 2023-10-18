import random as rn
import pandas as pd

df = pd.read_csv("Books.csv", low_memory=False)
ratings = [rn.randint(1, 10) for _ in range(len(df))]
price = [rn.randint(20, 50) for _ in range(len(df))]

df["Ratings"] = ratings
df["Price"] = price

df.to_csv("Books.csv", index=False)
print("Finished!")
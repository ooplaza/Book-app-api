import random as rn
import pandas as pd


def run():
    df = pd.read_csv("./Datasets/Books.csv", low_memory=False)
    for index, data in enumerate(df["RELEASE_YEAR"]):
        if data == 'Gallimard':
            print(f"{index} - {data}")
            df.loc[index, "RELEASE_YEAR"] = 2000
    df.to_csv("Books.csv", index=False)
    print("Finished!")

# def run():
#     df = pd.read_csv("./Datasets/Books.csv", low_memory=False)
#     ratings = [rn.randint(1, 10) for _ in range(len(df))]
#     price = [rn.randint(20, 50) for _ in range(len(df))]
#
#     df["Ratings"] = ratings
#     df["Price"] = price
#
#     df.to_csv("Books.csv", index=False)
#     print("Finished!")

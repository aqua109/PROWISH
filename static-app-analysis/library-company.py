import pandas as pd

df = pd.read_csv("distinct_libraries.csv")

print(df.head)

# for index, library in df["Library"].items():
#     try:
#         first_index = library.index(".")
#         second_index = library.index(".", first_index + 1)
        
#         prefix = library[:second_index]

#         print(prefix)
#         df.loc[index, ['Prefix']] = [f"{prefix}"]

#     except ValueError as e:
#         continue

# df.to_csv("distinct_libraries.csv", index=False)


for index, prefix in df["Prefix"].items():

    if (len(prefix) == 5):
        print(prefix)
        df.loc[index, ["Company"]] = ["False"]
    # try:
    #     first_index = library.index(".")
    #     second_index = library.index(".", first_index + 1)
        
    #     prefix = library[:second_index]

    #     print(prefix)
    #     df.loc[index, ['Prefix']] = [f"{prefix}"]

    # except ValueError as e:
    #     continue


df.to_csv("distinct_libraries.csv", index=False)
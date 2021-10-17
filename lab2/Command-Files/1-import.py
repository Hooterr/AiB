import pandas as pd

df = pd.read_csv('../Original-Data/earthquake_data.csv')

df.columns = ["1","2","3","4","5","6","7","age","sex","income","region"]

df = df.melt(id_vars=["sex","income","region", "age"], value_vars=["1","2","3","4","5","6","7"], var_name="question", value_name="answer")

df.to_csv('../Analysis-Data/1-QA.csv')


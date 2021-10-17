import pandas as pd

df = pd.read_csv('../Analysis-Data/1-QA.csv')

# filter question 3
df = df.loc[df['question'] == 3]
df = df[['age', 'sex','answer']]
df.to_csv('../Analysis-Data/2-Q3.csv')


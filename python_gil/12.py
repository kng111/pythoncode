import pandas as pd 

data = {'Name': ["Alice","bob","Alice","bob","alice"],
        'Subject': ['Math','Math','Science','Science','Math'],
        'Score': [90,85,88,92,95]}

df = pd.DataFrame(data)
pivot_tavle = pd.pivot_table(df, values='Score', index='Name',columns='Subject', aggfunc='mean')
print(pivot_tavle)
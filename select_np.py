import pandas as pd

data = {
    'Score': [85, 60, 45, 75, 90, 30],
    'Grade': [''] * 6  # Empty column for storing the categorized values
}

df = pd.DataFrame(data)
print(df)



import numpy as np

conditions = [
    df['Score'] >= 90,
    (df['Score'] >= 80) & (df['Score'] < 90),
    (df['Score'] >= 70) & (df['Score'] < 80),
    (df['Score'] >= 60) & (df['Score'] < 70),
    df['Score'] < 60
]

grades = ['A', 'B', 'C', 'D', 'F']

df['Grade'] = np.select(conditions, grades, default='Unknown')
print(df)
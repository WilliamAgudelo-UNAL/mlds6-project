# -*- coding: utf-8 -*-
"""main.ipynb
   Código de la carga de datos
"""

import pandas as pd
df = pd.read_excel('../../data/Subject_Demographics_and_Analysed_Data.xlsx')
df = df.iloc[1:].copy() # Drop the first row (index 0) containing units and create a copy to avoid SettingWithCopyWarning

df['Subject Age'] = pd.to_numeric(df['Subject Age'], errors='coerce')
df['PSA'] = pd.to_numeric(df['PSA'], errors='coerce')

# Explicitly iterate and convert each column in the range 8 to 27 (indices 8 to 27)
for col_idx in range(8, 28):
    col_name = df.columns[col_idx]
    df[col_name] = pd.to_numeric(df[col_name], errors='coerce')

df.head()

data_dict = pd.DataFrame({
    'Column': df.columns,
    'DataType': df.dtypes,
    'UniqueValues': [df[col].nunique() for col in df.columns]
})
print(data_dict)


# Set pandas display options to prevent truncation
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', None)       # Adjust display width to fit content
pd.set_option('display.max_rows', None)    # Display all rows (if describe() output had many rows)
pd.set_option('display.float_format', lambda x: '%.3f' % x) # Optional: format floats
print(df.describe())

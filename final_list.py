import pandas as pd


df1 = pd.read_excel('api_author.xlsx')
df2 = pd.read_excel('api_location.xlsx')

columns_df1 = df1[['Title', 'Author']]
columns_df2 = df2[['University']]

merge_df = pd.concat([columns_df1, columns_df2], axis=1)
merge_df.to_excel('final_list.xlsx', index=False)
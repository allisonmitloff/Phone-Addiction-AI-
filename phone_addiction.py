import pandas as pd
df = pd.read_csv('allison.csv')
unique_values = ['screen_time', 'social_networking', 'education', 'productivity', 'health', 'entertainment']
df.columns = unique_values
# resample the dataframe
df1 = df[df['productivity']=='Productive']
df2 = df[df['productivity']=='Not Productive']
# length of the dataframe
len_df1 = len(df1)
len_df2 = len(df2)
print(len_df1)
print(len_df2)
df_resampled = pd.concat([df1,df2.sample(n=len_df1, replace=True)])
# write the dataframe
df_resampled.to_csv('filename.csv', index=False)
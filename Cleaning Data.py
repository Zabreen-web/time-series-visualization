import pandas as pd
df=pd.read_csv('un-country-data.csv')
#cleaning data
countries=df[df['ISO3_code'].notnull()]

columns=['ISO3_code','Location','Time','TPopulation1Jan','TPopulation1July']
clean_df=countries[columns]
clean_df.to_csv('cleaned-data.csv')


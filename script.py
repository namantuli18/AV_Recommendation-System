import pandas as pd
import numpy as np
df=pd.read_csv('train.csv')
#print(df.head())
user_ids=df.user_id.unique()
#print(user_ids)
for rows,count in enumerate(df.user_id):
	for ids in user_ids:
		if ids==rows:
			print(rows,ids)
			break
	print(count)
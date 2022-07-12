import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df=pd.read_csv('FEH_00200524_220712104723.csv',index_col='全国・都道府県',encoding='shift_jis')

df=df.drop('全国',axis=0)

df['2021年']=pd.to_numeric(df['2021年'].str.replace(",",""))
df['2020年']=pd.to_numeric(df['2020年'].str.replace(",",""))

df['人口増減']=df['2021年'] - df['2020年']



#print(df['2021年'])

df=df.sort_values('人口増減',ascending=False)

df['人口増減'].plot.bar(figsize=(10,6))
#plt.ylim(-50,14000)
plt.show()



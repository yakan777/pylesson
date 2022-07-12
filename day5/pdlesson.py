import pandas as pd

df=pd.read_csv("test.csv")
print(df)

print('件数:',len(df))
print('項目名:',df.columns.values)
print('index:',df.index.values)

print('----行の取り出し----')

print('行index',df.loc[2])
print('行index',df.loc[[3,4]])
print('value',df.loc[2]['国語'])
print('value',df.loc[2,'国語'])
print('value',df.iloc[2,3])

print('----列の取り出し----')

print('列名',df['国語'])
print('列名',df[['国語','理科']])

print('----1行データの追加----')
df.loc[6]=['G恵',90,92,94,96,92]
print(df)

print('----1列データの追加----')
df['美術']=[68,73,82,77,94,96,98]
print(df)

print('----データの更新(1つの値)----')
df.loc[0,'国語']=85
df.loc[0]['国語']=85
print(df)

print('----データの更新(1つの行)----')
df.loc[0]=['A太',82,90,76,97,76,70]
print(df)
print('----データの更新(1つの列)----')
df['美術']=[69,74,83,78,95,97,99]
print(df)

import pandas as pd
import folium


m=folium.Map(location=[35.942957,136.198863],zoom_start=16)
df=pd.read_csv('936.csv',encoding='shift-jis')
buss=df[['緯度','経度',]].values

for data in buss:
    folium.Marker([data[0],data[1]]).add_to(m)
m.save('buss.html')

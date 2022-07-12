import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df=pd.read_csv('test.csv',index_col=0)

#国語
df['国語'].plot.barh()
plt.legend(loc='lower left')
plt.show()

#国語と数学
df[['国語','数学']].plot.barh()
plt.legend(loc='lower left')
plt.show()

#c子
df.loc['C子'].plot.barh()
plt.legend(loc='lower left')
plt.show()

#c子
df.loc['C子'].plot.pie(labeldistance=0.6)
plt.legend(loc='lower left')
plt.show()

df.T.plot.bar()
plt.legend(loc='lower right')
plt.savefig('bargraph.png')

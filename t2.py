import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
df = pd.read_csv("d2\california_cities.csv")
print(df.head())

df = df.dropna(subset='elevation_m')
colunas_exclusao = ['elevation_ft']

df = df.drop(colunas_exclusao,axis=1)

latitude, longitude = df['latd'], df['longd']
population, area = df["population_total"], df['area_total_km2']

plt.scatter(longitude,latitude, label=None, c=np.log10(population),cmap='viridis',s=area,linewidth=0,alpha=0.5)
plt.axis('equal')
plt.xlabel("latitude")
plt.ylabel('longitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3,7)

for area in [100, 300, 500]:
    plt.scatter([],[], c="k",alpha=0.3,s=area,label=str(area) + 'km$2$')

plt.legend(scatterpoints=1,frameon=False,labelspacing= 1,title="Area da cidade")
plt.title("area e população das cidades da california")
plt.show()
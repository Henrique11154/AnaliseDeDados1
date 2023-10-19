import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
df = pd.read_csv('desafio001\president_heights.csv')
print(df.head())

height = np.array(df['height(cm)'])
print(height)

print('media das alturas =:',round(height.mean(),2))

print("Altura minima: ",height.min())

plt.hist(height)
plt.title("Altura dos presidentes EUA")
plt.xlabel("Altura")
plt.ylabel("numero")
plt.show()
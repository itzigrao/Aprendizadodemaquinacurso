# %% 

import pandas as pd

df = pd.read_parquet("dados/dados_clones.parquet") # Ler os dados do arquivo Parquet

df['General Jedi encarregado'].unique()

df.head()

#%%

features = ['Massa(em kilos)', 'Estatura(cm)']
target = 'Status '
df.groupby(target)[features].mean()

# %%

X = df[features] 
y = df[target]


# %%

from sklearn import tree



model = tree.DecisionTreeClassifier(max_depth=3, random_state=42) # max_depth define a profundidade máxima da árvore de decisão, e random_state garante que os resultados sejam reproduzíveis.


model.fit(X=X, y=y)
# %%

import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(model,feature_names=features, 
               class_names=model.classes_,
               filled=True)
# %%

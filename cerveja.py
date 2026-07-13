# %%

import pandas as pd

df = pd.read_excel("dados/dados_cerveja.xlsx") # Ler os dados do arquivo Excel
df.head()  # mostra as primeiras linhas do DataFrame para ter uma visão geral dos dados.

# %%

features = ['temperatura', 'copo', 'espuma', 'cor'] # Lista de características
target = 'classe' # Variável alvo

X = df[features] 
y = df[target]

X = X.replace({ # Substituir valores por números por que a maquina so faz leitura em numeros
    "mud":1, "pint":2,
    "sim":1, "não":0,
    "clara":0, "escura":1
})

# %%

from sklearn import tree

model = tree.DecisionTreeClassifier()

model.fit(X=X, y=y)


# %%

# a baixo vai mostrar a arvore de decisão gerada pelo modelo, com as características e classes correspondentes.
import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(model,feature_names=features, 
               class_names=model.classes_,
               filled=True)

# %%

#primeiro algoritmo de aprendizagem de maquina (machine learning).
# %%

import pandas as pd

df = pd.read_excel("dados/dados_frutas.xlsx")
df

# %%

from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)

# %%

y = df['Fruta']

caracteristicas = ['Arredondada','Suculenta', 'Vermelha', 'Doce']
x = df[caracteristicas]





# %%

#ISSO AQUI E MACHINE LEARNING

arvore.fit(x, y) #vai criar a árvore de decisão com base nos dados de entrada (x) e nas classes (y). 

# %%
arvore.predict([[0, 0, 0, 0]]) #cada elemento corresponde a uma caracteristica

# %%

import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(arvore,
               feature_names=caracteristicas,
               class_names=arvore.classes_,
               filled=True)

# %%

proba = arvore.predict_proba([[1, 1, 1, 1]])[0] #vai retornar a probabilidade de cada classe para a entrada fornecida.
pd.Series(proba, index=arvore.classes_)

# %%

# %%

import pandas as pd 

df = pd.read_excel("dados/dados_cerveja_nota.xlsx")
df.head()

# %%

from sklearn import linear_model

X = df[['cerveja']] # X maiuscula porque é uma matriz, um vetor bidimensional. Matriz (dataframe)
y = df['nota'] # uma target, utilizamos como um vetor que queremos prever. # VEtor (séries)

#em livros de estatitica, x são as matrizes e y vetores.

# ISSO AQUI É O APRENDIZADO DE MAQUINA.

reg = linear_model.LinearRegression() #escolhendo o modelo de regressão linear.

reg.fit(X, y) # modelo ajustado

# %%

a, b = reg.intercept_, reg.coef_[0]
print(a, b)

#mostrando quais são os coeficientes.


# %%

predict = reg.predict(X.drop_duplicates()) #novas predições

import matplotlib.pyplot as plt 

plt.plot(X['cerveja'],y, 'o')
plt.grid(True)
plt.title("Relação Cerveja vs Nota")
plt.xlabel("Cerveja")
plt.ylabel("Nota")

plt.plot(X.drop_duplicates()['cerveja'], predict)

plt.legend(['Observado', f'y = {a:.3f} + {b:.3f}x' ])
# %%

# função = f(x) = y  
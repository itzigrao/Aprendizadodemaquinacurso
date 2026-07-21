# %%
import pandas as pd 
import matplotlib.pyplot as plt


# %%
df = pd.read_excel("dados/dados_cerveja_nota.xlsx")    
df.head()

df['aprovado'] = (df['nota'] > 5).astype(int)

# %%

plt.plot(df['cerveja'], df['aprovado'], 'o', color='royalblue')
plt.grid(True)
plt.title('cerveja vs notas')
plt.xlabel('cerveja')
plt.ylabel('nota')


# %%

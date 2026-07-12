# %%
import sys
import pandas as pd

print("Python utilizado:")
print(sys.executable)

print("Versão do pandas:")
print(pd.__version__)


# %%
dados = {
    "fruta": ["maçã", "banana", "laranja"],
    "peso": [130, 110, 160]
}

df = pd.DataFrame(dados)

df
# %%

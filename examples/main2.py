import pandas as pd

# Exemplo inicial
df = pd.DataFrame([
    ["id", "nome", "idade"],   # <- esta linha será usada como header
    [1, "Ana", 25],
    [2, "Bruno", 30],
    [3, "Carlos", 40]
])

print("Antes:\n", df)

nova_linha = pd.DataFrame([['lin0', "lin1", 'lin3']], columns=df.columns)
df = pd.concat([nova_linha, df], ignore_index=True)


# 1. Pega a primeira linha como header
df.columns = df.iloc[0]

# 2. Remove a primeira linha
df = df.drop(index=0).reset_index(drop=True)

print("\nDepois:\n", df)
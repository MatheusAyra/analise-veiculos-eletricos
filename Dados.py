import pandas as pd

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

print(df.head())

print(df.describe())

print(df.info())

print(df.isnull().sum())

# Count the total number of electric vehicles
total_electric_vehicles = df.shape[0]
print("Total Electric Vehicles:", total_electric_vehicles)

filtered_recent = df[df['Model Year'] >= 2020]
print(filtered_recent.head())

#Vamos verificar a quantidade de veículos elétricos por estado
# Contar veículos por marca
brand_counts = df['Make'].value_counts()
print("Marcas mais populares de veículos elétricos:")
print(brand_counts)

# Se quiser ver só as 10 mais populares:
print("Top 10 marcas:")
print(brand_counts.head(10))

import matplotlib.pyplot as plt

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# ...existing code...

# Top 10 marcas
top_10_brands = df['Make'].value_counts().head(10)

plt.figure(figsize=(10,6))
bars = plt.bar(top_10_brands.index, top_10_brands.values, color='#4F81BD', edgecolor='black')
plt.title('Top 10 Marcas de Veículos Elétricos', fontsize=16, fontweight='bold')
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Quantidade', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adiciona valores nas barras
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), int(bar.get_height()),
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

plt.tight_layout()
plt.show()

# Top 10 estados com mais veículos elétricos
state_counts = df['State'].value_counts().head(10)

plt.figure(figsize=(10,6))
bars = plt.bar(state_counts.index, state_counts.values, color='#F28E2B', edgecolor='black')
plt.title('Top 10 Estados com Veículos Elétricos', fontsize=16, fontweight='bold')
plt.xlabel('Estado', fontsize=14)
plt.ylabel('Quantidade', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adiciona valores nas barras
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), int(bar.get_height()),
             ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

plt.tight_layout()
plt.show()

# Gráfico de barras
plt.figure(figsize=(10,6))
top_10_brands.plot(kind='bar')
plt.title('Top 10 Marcas de Veículos Elétricos')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# ...existing code...

# Top 10 estados com mais veículos elétricos
state_counts = df['State'].value_counts()
print("Estados com mais veículos elétricos:")
print(state_counts)

print("Top 10 estados:")
print(state_counts.head(10))

# Gráfico de barras para os 10 estados
plt.figure(figsize=(10,6))
state_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Estados com Veículos Elétricos')
plt.xlabel('Estado')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ...existing code...
import pandas as pd
import matplotlib.pyplot as plt


# Läs in datan
df = pd.read_csv("data/penguins.csv")

print("Första raderna:")
print(df.head())

print("\nInfo om kolumnerna:")
print(df.info())

print("\nStatistisk sammanfattning:")
print(df.describe())

print("\nMedelvikt per art:")
print(df.groupby("species")["body_mass_g"].mean())

# Enkelt diagram: medelvikt per art
avg_mass = df.groupby("species")["body_mass_g"].mean()
avg_mass.plot(kind="bar", title="Medelvikt per pingvinart (g)")
plt.ylabel("Vikt (g)")
plt.tight_layout()
plt.savefig("results/medelvikt_per_art.png")
print("\nDiagram sparat i results/medelvikt_per_art.png")

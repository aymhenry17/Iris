import pandas as pd
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine
import time

# Attendre que la base de données soit prête
time.sleep(10)

# Lire le CSV
df = pd.read_csv('/data/iris.csv')
df = df[['sepal_length', 'sepal_width']].dropna()

# Normaliser
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Connexion à la base PostgreSQL
engine = create_engine('postgresql://postgres:postgres@db:5432/irisdb')
df_scaled.to_sql('iris_data', engine, if_exists='replace', index=False)

print("✅ Données insérées dans PostgreSQL.")
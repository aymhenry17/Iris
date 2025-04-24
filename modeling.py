import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

# Mise à jour de la configuration de la connexion PostgreSQL
db_user = 'postgres'
db_password = 'postgres'
db_host = 'localhost'
db_port = '5432'
db_name = 'irisdb'
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(db_url)

# Extraction des données
requete = "SELECT * FROM iris_data"  # Remplacez 'votre_table' par le nom de votre table
data = pd.read_sql(requete, con=engine)

# Préparation des données
# Supposons que la colonne cible soit la dernière colonne ; modifiez si nécessaire
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Définition de l'expérience MLflow
mlflow.set_experiment("iris_regression_experiment")

with mlflow.start_run():
    # Entraînement du modèle RandomForestRegressor
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Prédictions sur l'ensemble de test
    y_pred = model.predict(X_test)
    
    # Calcul des métriques
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Enregistrement des métriques dans MLflow
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)
    
    # Enregistrement du modèle dans MLflow
    mlflow.sklearn.log_model(model, "random_forest_model")
    
    print("Modèle entraîné et enregistré avec succès !")
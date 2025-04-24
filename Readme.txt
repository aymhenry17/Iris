## Service 1 — Prétraitement des données

Responsable : Alice

### Étapes réalisées :
- Lecture du fichier `iris.csv` fourni
- Sélection des colonnes `sepal_length` et `sepal_width`
- Nettoyage des valeurs manquantes
- Normalisation des données via `StandardScaler`
- Insertion des données normalisées dans une base PostgreSQL

### Technologies utilisées :
- Python
- Pandas
- scikit-learn
- SQLAlchemy
- PostgreSQL
- Docker

### Conteneur :
- Nom du service Docker : `preprocessing`
- Ce service est lancé automatiquement par `docker-compose up`
- Il attend que PostgreSQL soit prêt, puis insère les données dans la table `iris_data`
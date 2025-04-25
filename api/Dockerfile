FROM python:3.10

# Définit le répertoire de travail
WORKDIR /app

# Copie tous les fichiers dans le répertoire de travail du conteneur
# COPY . /app
COPY requirements.txt /app/requirements.txt
# Installe les dépendances définies dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exécute le script main.py au démarrage du conteneur
CMD ["python", "main.py"]

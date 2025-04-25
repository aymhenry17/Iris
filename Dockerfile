# Dockerfile

FROM python:3.10-slim

# Crée un dossier pour l'app
WORKDIR /app

# Copie les fichiers nécessaires
COPY . /app

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port pour FastAPI
EXPOSE 8000

# Commande pour lancer FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

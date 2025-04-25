import os
import mlflow.sklearn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import numpy as np

app = FastAPI()

# 👇 Input attendu par la route /predict
class SepalInput(BaseModel):
    sepal_width: float

# Définir le run_id (ou récupère-le dynamiquement comme expliqué plus tôt)
run_id = "ba91b41a462f4c89a9fd0e841560d88b"  # Remplacez par ton run_id
MODEL_PATH = f"mlruns/177564898664332604/{run_id}/artifacts/random_forest_model"
# MODEL_PATH = f"mlruns/0/{run_id}/artifacts/model"
# mlruns\177564898664332604\ba91b41a462f4c89a9fd0e841560d88b\artifacts\random_forest_model\model.pkl


# Vérification de l'existence du modèle avant de le charger
if not os.path.exists(MODEL_PATH):
    raise Exception(f"Le modèle n'a pas été trouvé à {MODEL_PATH}")

# Charger le modèle
model = mlflow.sklearn.load_model(MODEL_PATH)

@app.post("/predict")
def predict(input: SepalInput) -> Dict[str, float]:
    if input.sepal_width <= 0:
        raise HTTPException(status_code=400, detail="La largeur du sépale doit être positive.")
    try:
        prediction = model.predict(np.array([[input.sepal_width]]))
        return {"sepal_length": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
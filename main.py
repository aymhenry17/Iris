from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import mlflow.sklearn
import numpy as np

app = FastAPI()

# 👇 Input attendu par la route /predict
class SepalInput(BaseModel):
    sepal_width: float

MODEL_PATH = "mlruns/0/<ton_run_id>/artifacts/model"
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


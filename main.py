from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import pandas as pd
from components.customFile import CustomFile
import numpy as np

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

cfile = CustomFile()
symptoms = cfile.getFeatures()
encoder = cfile.getEncoder()
predictionClass = cfile.getPredictionClasses()

@app.get("/")
def root(request: Request):
    # cfile = CustomFile()
    # symptoms = cfile.getFeatures()
    # print(encoder)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "symptoms": symptoms
    })

@app.post("/")
async def generate_table(request: Request):
    form = await request.form()
    checked_symptoms = form.getlist("symptom")
    error = False

    if len(checked_symptoms) < 3:
        error = True

    model = cfile.nb_model

    input_data = [0] * len(encoder)
    for symptom in checked_symptoms:
        index = encoder[symptom]
        input_data[index] = 1

    input_data = np.array(input_data).reshape(1,-1)

    result_index = model.predict(input_data)[0]
    result = predictionClass[result_index]

    print(result)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "symptoms": symptoms,
        "checkedSymptoms": checked_symptoms,
        "result": result,
        "error": error
    })

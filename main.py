from enum import Enum

from fastapi import FastAPI
from TrackerDB import Tracker  # Importo la mia classe
from pydantic import BaseModel, Field
from datetime import date

class LiftValido(str, Enum):
    muscle_up = "muscle_up"
    pull_up = "pull_up"
    dip = "dip"
    squat = "squat"

# Type hints, servono per validare i dati, se mando dati sbagliati se ne accorge da qui
class NuovoLift(BaseModel):
    data: date   # <-- verifica che sia una data
    lift: LiftValido  # Permette di verificare se un lift fa parte di quelle 4 categorie
    peso: int = Field(ge=0, le=500)  # ge = greater-equal le = less equal, quindi un peso deve essere >= 0 e <= 500
    reps: int = Field(ge=1, le=100)  # le reps devono essere >= 1 e <= 100

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Tracker Street Lifting API"}

@app.get("/massimali")
def get_massimali():
    tracker = Tracker("allenamenti.db")
    dati = tracker.massimali_dict()  # Nuovo metodo per ottenere i dati in formato dizionario
    tracker.chiudi()
    return dati

@app.post("/sessioni")
def aggiungi_sessione(nuovo: NuovoLift):    # I dati avranno la forma della classe "NuovoLift", controlla quindi se è valido
    tracker = Tracker("allenamenti.db")
    tracker.aggiungi_lift(str(nuovo.data), nuovo.lift, nuovo.peso, nuovo.reps)  # Se è valido è già passato come oggetto
    tracker.chiudi()
    return {"stato":"aggiunto", "lift": nuovo.lift}





# py -m venv venv
# venv\Scripts\activate
# pip install fastapi uvicorn
# uvicorn main:app --reload  <-- per ricaricare il server dopo le modifiche fatte
# pip freeze > requirements.txt  <-- per conservare i requisiti per questo progettoù

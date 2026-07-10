import json

# ---------------- INIZIO CLASSE TRACKER -----------------------

class Tracker:
    def __init__(self, nome):  # Costruttore classe Tracker
        self.nomeFile = nome
        self.sessioni = []  # Inizializziamo la lista vuota
        self.carica()   # Se esiste, carica dal file JSON tutte le sessioni all'interno della lista "sessioni"

    def carica(self):   # Carica, se c'è, una sessione precedente
        try:  # Proviamo a vedere se il file JSON esiste
            with open(self.nomeFile, "r") as j:
                self.sessioni = json.load(j)  # Converte le sessioni dal formato JSON in lista
        except (FileNotFoundError, json.JSONDecodeError):  # Se non la trova semplicemente la lista è vuota, catturando l'errore
            self.sessioni = []

    def salva(self):   # Salva tutta la lista nel JSON
        with open(self.nomeFile, "w") as j:
            json.dump(self.sessioni, j)  # Converte la lista in formato JSON

    def aggiungi_sessione(self, sessione):   # Aggiunge una sessione alla lista
        self.sessioni.append(sessione)
        self.salva()  # Salva sempre

    def mostra_storico(self):   # Mostra lo storico di tutte le sessioni
        for data in self.sessioni:
            print("\n------------------------------")
            for chiave, valore in data.items():
                print(chiave + ": ", end="")
                if chiave == "lift":  # La chiave lift presenta al suo interno un altro dizionario
                    for esercizio, specifiche in valore.items():  # A loro volta ogni esercizio "Chiave" ha come valore un altro dizionario che accediamo con la chiave direttamente
                        print(f"\n{esercizio} : peso: {specifiche['peso']}, reps: {specifiche['reps']}", end="")
                else:
                    print(valore)  # Sennò stampiamo il valore normale (la data del campo "data")

    def progresso(self, lift):  # Mostra il progresso di una alzata in particolare
        print("\n------------------------------")
        print("Progresso " + lift + ":")
        for campo in self.sessioni:
            data = campo["data"]
            specifiche = campo["lift"].get(lift)
            if specifiche is None:
                continue  # salta questa sessione che il lift qui non c'è
            print(f"{data}: {specifiche['peso']}kg x {specifiche['reps']}")
        print("------------------------------")

# ---------------- FINE CLASSE TRACKER -----------------------

# ------------ INIZIO MAIN ---------------------------

if __name__ == "__main__":
    tracker = Tracker("MattiaLifts.json")
    sessione = {
        "data": "2026-07-06",
        "lift": {
            "muscle_up": {"peso": 10, "reps": 5},
            "pull_up":   {"peso": 20, "reps": 8},
            "dip":       {"peso": 25, "reps": 10},
            "squat":     {"peso": 80, "reps": 5}
        }
    }
    tracker.mostra_storico()
    tracker.progresso("muscle_up")
    tracker.salva()

# ------------ FINE MAIN ---------------------------
# Street Lifting Tracker

Tracker da riga di comando per i miei allenamenti di street lifting, nel formato ISF
(muscle-up, pull-up, dip, squat). Permette di registrare peso e ripetizioni di ogni
esercizio in ogni sessione, e di visualizzare progressi e massimali.

Progetto di apprendimento, implementato in due versioni:

1. Con persistenza su file JSON
2. Con persistenza su database SQLite

> Nota: i dati generati da `crea_database.py` sono casuali e non corrispondono
> ai miei allenamenti reali.

## Utilizzo

Versione SQLite (consigliata):

```bash
python TrackerDB.py
```

Versione JSON:

```bash
python TrackerJSON.py
```

Per generare un database di esempio con dati di prova:

```bash
python crea_database.py
```

Per avviare il server web di prova:

```bash
uvicorn main:app --reload
```

## Perché due versioni

La prima implementazione salvava i dati in un file JSON, caricando l'intero storico
in memoria a ogni avvio. Funziona, ma ogni interrogazione sui dati (per esempio la
progressione dello squat) richiedeva di scrivere a mano cicli e filtri in Python.

La seconda versione usa SQLite. Il metodo `progresso()` è passato da otto righe di
logica Python a una singola query:

```sql
SELECT data, peso, reps FROM sessioni WHERE lift = ? ORDER BY data
```

Vantaggi concreti del passaggio:

- Filtri e ordinamenti eseguiti dal database, senza caricare tutto in memoria
- Aggregazioni (massimali, medie, volume) in una riga con `GROUP BY`
- Nessuna gestione manuale di lettura, scrittura e file corrotti
- Query parametrizzate con `?` contro le SQL injection

## API REST

La versione SQLite è esposta anche come API web tramite FastAPI (`main.py`), con
validazione dei dati in ingresso tramite Pydantic. Una volta avviato il server,
la documentazione interattiva è disponibile su `http://127.0.0.1:8000/docs`.

Endpoint principali:

- `GET /massimali` — restituisce il massimale per ogni lift
- `POST /sessioni` — registra un nuovo allenamento (con validazione)

## Struttura dei dati

Nella versione JSON i dati sono annidati: una sessione contiene i quattro lift.
In SQLite sono appiattiti, ogni riga è un lift in una sessione identificato da data
ed esercizio. Questo rende immediate le query per singolo lift.

## Stack

Python 3, SQLite (modulo `sqlite3` della libreria standard), FastAPI e Pydantic
per l'API REST. Le dipendenze sono in `requirements.txt`.
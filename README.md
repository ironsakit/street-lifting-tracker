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
python tracker_sqlite.py
```

Versione JSON:

```bash
python tracker_json.py
```

Per generare un database di esempio con dati di prova:

```bash
python crea_database.py
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

## Struttura dei dati

Nella versione JSON i dati sono annidati: una sessione contiene i quattro lift.
In SQLite sono appiattiti, ogni riga è un lift in una sessione identificato da data
ed esercizio. Questo rende immediate le query per singolo lift.

## Stack

Python 3, SQLite (modulo `sqlite3` della libreria standard). Nessuna dipendenza esterna.
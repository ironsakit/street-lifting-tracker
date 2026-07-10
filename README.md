\# Street Lifting Tracker



Si tratta di un Tracker da riga di comando dei miei allenamenti di Street Lifting

(ovviamente i dati all'interno di 'crea\_database' sono casuali e non c'entrano nulla con i miei allenamenti veri).

I dati sono registrati all'interno di un JSON oppure all'interno di una tabella in un database, nel formato ISF:

muscle-up, pull-up, dip, squat). Permette di registrare peso e ripetizioni di ogni singolo esercizio in ogni

mia sessione di allenamento e mostra progressi e massimali.



Questo è un progetto di apprendimento: implementato in due versioni:

1\) Con persistenza su JSON.

2\) Con persistenza su DB SQLite.



\## Utilizzo



Versione SQLite (consigliata):

```bash

python tracker\_sqlite.py

```



Versione JSON:

```bash

python tracker\_json.py

```



Per generare un database di esempio con dati di prova:

```bash

python crea\_database.py

```



\## Perché due versioni?



La prima implementazione salvava i dati in un file JSON, caricando l'intero

storico in memoria ad ogni avvio. Funziona, ma ogni interrogazione sui dati

(come la "progressione sugli squat") richiedeva di scrivere a mano

cicli e filtri in Python.



La seconda versione usa SQLite. Il metodo `progresso()` è passato da 8

righe di logica Python a una singola query:



```sql

SELECT data, peso, reps FROM sessioni WHERE lift = ? ORDER BY data

```



Molto più ordinato, compatto ed efficiente.



\## Struttura dei dati



Nella versione JSON i dati sono annidati (una sessione contiene i quattro lift).

In SQLite sono appiattiti: ogni riga è un lift in una sessione, identificato da

data ed esercizio, questo rende immediate le query per singolo lift.



\## Stack



Python 3, SQLite (modulo `sqlite3` della libreria standard). Nessuna dipendenza esterna.


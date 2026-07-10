import sqlite3

class Tracker:
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome)
        self.cursor = self.conn.cursor()
        self.crea_tabella()    # Crea la tabella se non esiste già

    def crea_tabella(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessioni (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            lift TEXT NOT NULL,
            peso INTEGER NOT NULL,
            reps INTEGER NOT NULL
        )""")
        self.conn.commit()

    def aggiungi_lift(self, data, lift, peso, reps):
        self.cursor.execute("INSERT INTO sessioni (data, lift, peso, reps) VALUES (?, ?, ?, ?)",
                            (data, lift, peso, reps))
        self.conn.commit()

    def massimali(self):
        self.cursor.execute("SELECT lift, MAX(peso) as massimale FROM sessioni GROUP BY lift")
        print("--- Massimale per ogni lift: ---")
        for lift, massimale in self.cursor.fetchall():
            print(f"{lift} --> {massimale}kg")

    def progresso(self, lift):
        self.cursor.execute("SELECT data, peso, reps FROM sessioni WHERE lift = ? ORDER BY data", (lift,))
        for data, peso, reps in self.cursor.fetchall():
            print(f"{data}: {lift} --> {peso}kg x {reps}")


    def chiudi(self):
        self.conn.close()


if __name__ == "__main__":
    tracker = Tracker("allenamenti.db")
    tracker.progresso("muscle_up")
    #tracker.aggiungi_lift("2026-07-09", "muscle_up", 12, 5)
    #tracker.aggiungi_lift("2026-07-09", "squat", 85, 5)
    tracker.massimali()
    tracker.chiudi()
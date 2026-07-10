import os.path, sqlite3

DB = "allenamenti.db"

if os.path.exists(DB):
    os.remove(DB)

conn = sqlite3.connect("allenamenti.db")
cursor = conn.cursor()
cursor.execute("""
        CREATE TABLE sessioni (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            lift TEXT NOT NULL,
            peso INTEGER NOT NULL,
            reps INTEGER NOT NULL
        )""")

dati = [  # dati fittizi
    ("2026-05-04", "muscle_up",  8,  4), ("2026-05-04", "pull_up", 15, 8),
    ("2026-05-04", "dip", 20, 10),       ("2026-05-04", "squat", 70, 5),
    ("2026-05-11", "muscle_up", 10,  4), ("2026-05-11", "pull_up", 17, 8),
    ("2026-05-11", "dip", 22, 10),       ("2026-05-11", "squat", 75, 5),
    ("2026-05-18", "muscle_up", 10,  5), ("2026-05-18", "pull_up", 20, 7),
    ("2026-05-18", "dip", 25,  9),       ("2026-05-18", "squat", 80, 5),
    ("2026-05-25", "muscle_up", 12,  4), ("2026-05-25", "pull_up", 20, 9),
    ("2026-05-25", "dip", 25, 11),       ("2026-05-25", "squat", 82, 4),
    ("2026-06-01", "muscle_up", 12,  5), ("2026-06-01", "pull_up", 22, 8),
    ("2026-06-01", "dip", 27, 10),       ("2026-06-01", "squat", 85, 5),
    ("2026-06-08", "muscle_up", 14,  4), ("2026-06-08", "pull_up", 24, 7),
    ("2026-06-08", "dip", 30,  9),       ("2026-06-08", "squat", 87, 4),
    ("2026-06-15", "muscle_up", 14,  5), ("2026-06-15", "pull_up", 25, 8),
    ("2026-06-15", "dip", 30, 10),       ("2026-06-15", "squat", 90, 5),
    ("2026-06-22", "muscle_up", 15,  5), ("2026-06-22", "pull_up", 27, 7),
    ("2026-06-22", "dip", 32,  9),       ("2026-06-22", "squat", 92, 4),
]

cursor.executemany("INSERT INTO sessioni (data, lift, peso, reps) VALUES (?, ?, ?, ?)", dati)  # al posto di fare un ciclo uso executemany
conn.commit()
print(f"Database {DB} creato con {len(dati)} tuple")
conn.close()
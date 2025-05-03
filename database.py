import sqlite3

class Database:
    def __init__(self, db="database/listing.db"):
        self.db = db
        self._initialize_db()

    #connect to database
    def _connect(self):
        return sqlite3.connect(self.db)
    
    #initialize database
    def _initialize_db(self):
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS listings (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           description TEXT,
                           rent REAL,
                           address TEXT,
                           rooms INTEGER,
                           contact_info TEXT
                           )
                           ''')
            connection.commit()
    
    #insert listing into database
    def insert_listing(self,listing):
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                           INSERT INTO listings (title, description, rent, address, rooms, contact_info)
                           VALUES (?, ?, ?, ?, ?, ?)
                           ''', (listing["title"], listing["description"], listing["rent"], listing["address"], listing["rooms"], listing["contact_info"])) 
            connection.commit()

    #returns a python dictionary of all listings in the database
    def get_all_listings(self):
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM listings")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns,row)) for row in rows]
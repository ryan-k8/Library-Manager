import sqlite3
               
class Database:
    def __init__(self,db): #constructor - initialize the class of Database
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY,title varchar,author varchar,borrower varchar,doi date,price INTEGER,dor date)")
        self.conn.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM library")
        rows = self.cursor.fetchall()
        return rows
            
        
    def insert(self,title,author,borrower,doi,price,dor):
        self.cursor.execute("INSERT INTO library VALUES(NULL,?,?,?,?,?,?)",(title,author,
        borrower,doi,price,dor))
        self.conn.commit()
            
        
    def remove(self,id):
        self.cursor.execute("DELETE FROM library WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,borrower,doi,price,dor):
        self.cursor.execute("UPDATE library set title=?,author=?,borrower=?,doi=?,price=?,dor=? where id=?",(title,author,borrower,doi,price,dor,id))
        self.conn.commit()
        
    def __del__(self): #destructor - deinitialize the class of Database
        self.conn.close()

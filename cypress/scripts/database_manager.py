import sqlite3
import json
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path='test_data.db', table_name='data'):
        self.db_path = db_path
        self.table_name = table_name
        self._init_db()

    def _initDb(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   payload TEXT
                )
            """)
        
        conn.commit()
        conn.close()

    def save(self, data: dict):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
        INSERT INTO {self.table_name} (timestamp, payload)
        VALUES (?, ?)
    """, (datetime.now().isoformat(), json.dumps(data)))
        
        conn.commit()
        conn.close()

    def loadAll(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(f'SELECT id, timestamp, payload FROM {self.table_name}')
        rows = cursor.fetchall()
        
        conn.close()

        return [{'id': r[0], 'timestamp': r[1], 'data': json.dumps(r[2])} for r in rows]
    
    def loadById(self, record_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT id, timestamp, payload FROM {self.table_name} WHERE id = ?', (record_id))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {'id': row[0], 'timestamp': row[1], 'data': json.loads(row[2])}
        return None
    
    def loadByTime(self, start_time, end_time):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT id, timestamp, payload FROM {self.table_name} 
            WHERE timestamp BETWEEN ? AND ?
            """, (start_time, end_time))
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'timestamp': r[1], 'data': json.loads(r[2])} for r in rows]
    
    def loadByField(self, field_name, value):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT id, timestamp, payload FROM {self.table_name}')
        rows = cursor.fetchall()
        conn.close()
        result = []
        for r in rows:
            payload = json.loads(r[2])
            if payload.get(field_name) == value:
                result.append({'id': r[0], 'timestamp': r[1], 'data': payload})
        return result
    
    def updateRecrod(self, record_id, new_data: dict):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE {self.table_name}
            SET payload = ?, timestamp = ?
            WHERE id = ?
    """, (json.dumps(new_data), datetime.now().isoformat(), record_id))
        conn.commit()
        conn.close()

    def deleteRecord(self, record_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM {self.table_name} WHERE id = ?', (record_id))
        conn.commit()
        conn.close()

    def showLastN(self, n=3):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT id, timestamp, payload FROM {self.table_name} ORDER BY id DESC LIMIT ?', (n))
        rows = cursor.fetchall()
        conn.close()
        for r in rows:
            print(f'ID: {r[0]}, Timestamp: {r[1]}, Data:\n{json.dumps(json.loads(r[2]), indent=2, ensure_ascii=False)}')
            print('-' * 40)
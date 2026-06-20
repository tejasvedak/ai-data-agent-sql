import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect("sales.db")

    data = pd.DataFrame({
        "product": ["A","B","C","A","B","C"],
        "revenue": [100,200,150,120,180,220],
        "region": ["India","US","India","US","India","US"],
        "date": [
            "2024-01-01","2024-01-01","2024-01-02",
            "2024-01-02","2024-01-03","2024-01-03"
        ]
    })

    data.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    create_db()

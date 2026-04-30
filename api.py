from fastapi import FastAPI
import sqlite3

app = FastAPI(title="DealScout API")

@app.get("/api/latest-prices")
def get_prices():
    # Connect to the database you just built
    conn = sqlite3.connect("dealscout_data.db")
    cursor = conn.cursor()
    
    # Grab the 10 most recent price checks
    cursor.execute("SELECT timestamp, product_name, price FROM price_history ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    
    # Format it as clean JSON for the web
    results = [{"timestamp": r[0], "product": r[1], "price": r[2]} for r in rows]
    return {"status": "success", "data": results}
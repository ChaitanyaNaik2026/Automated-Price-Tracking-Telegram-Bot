import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def create_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            url TEXT,
            target_price FLOAT,
            last_price FLOAT
        )
    """)
    conn.commit()
    conn.close()

def insert_product(name, url, target_price, last_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (name, url, target_price, last_price)
        VALUES (%s, %s, %s, %s)
    """, (name, url, target_price, last_price))
    conn.commit()
    conn.close()

def update_product_name(product_id, name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name = %s WHERE id = %s", (name, product_id))
    conn.commit()
    conn.close()

def get_all_products():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_price(product_id, new_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET last_price = %s WHERE id = %s", (new_price, product_id))
    conn.commit()
    conn.close()

def delete_all_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products")
    conn.commit()
    conn.close()

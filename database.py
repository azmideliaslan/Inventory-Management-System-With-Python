# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 04:00:03 2022
@author: Azmi Deliaslan
"""
import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS
        products (
            "product_id"	INTEGER UNIQUE NOT NULL,
            "product_category"	TEXT NOT NULL,
            "product_brand"	TEXT NOT NULL,
            "product_name"	TEXT NOT NULL,
            "product_stock"	INTEGER NOT NULL,
            "cost_price"	NUMERIC NOT NULL,
            "selling_price"	NUMERIC NOT NULL,
	        PRIMARY KEY("product_id" AUTOINCREMENT)
        );
        """)
        self.conn.commit()

    def fetch_all_rows(self):
        self.cur.execute(
            """SELECT product_id, product_category , product_brand , product_name, product_stock, cost_price, selling_price FROM products""")
        rows = self.cur.fetchall()
        return rows

    def fetch_by_rowid(self, rowid):
        self.cur.execute(
            "SELECT rowid, product_id,product_category,product_brand, product_name, product_stock, cost_price, selling_price FROM products WHERE rowid=?", (rowid,))
        row = self.cur.fetchall()
        return row

    def fetch_by_product_id(self, product_id):
        self.cur.execute(
            "SELECT rowid, product_id,product_category,product_brand, product_name, product_stock, cost_price, selling_price FROM products WHERE product_id=?", (product_id,))
        row = self.cur.fetchall()
        return row

    def insert(self, product_id,product_category,product_brand, product_name, product_stock, cost_price, selling_price):
        self.cur.execute("""INSERT INTO products VALUES (?, ?, ?, ?, ?, ?,?)""",
                         (product_id, product_category, product_brand, product_name, product_stock, cost_price, selling_price))
        self.conn.commit()

    def remove(self, product_id):
        self.cur.execute(
            "DELETE FROM products WHERE product_id=?", (product_id, ))
        self.conn.commit()

    def update(self, rowid, product_id,product_category,product_brand, product_name, product_stock, cost_price, selling_price):
        self.cur.execute("""UPDATE products SET
            product_id=?,
            product_category=?,
            product_brand=?,
            product_name=?,
            product_stock=?,
            cost_price=?,
            selling_price=?
        WHERE
            rowid=?
        """, (product_id,product_category,product_brand, product_name, product_stock, cost_price, selling_price, rowid))
        self.conn.commit()

    # Defining a destructor to close connections
    def __del__(self):
        self.conn.close()


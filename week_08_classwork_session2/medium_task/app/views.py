from flask import flash, redirect, render_template, request, url_for
from app import app
import csv
import os
import datetime

'''
This function reads and returns the products.csv as a list.

header is an arg which allows you to decide whether you want to include the header
row or not - if you will need to write the data back into the file, you should
include the header row.

It defaults to header off.
'''
def read_products(header=False):
    products = []
    with  open(os.path.join(app.root_path, 'static', 'products.csv')) as f:
        prod_reader = csv.reader(f)
        for each in prod_reader:
            products.append(each)
    return products if header else products[1:]

def write_products(products):
    with open(os.path.join(app.root_path, 'static', 'products.csv'), mode="w", newline="") as f:
        writer = csv.writer(f)
        for row in products:
            writer.writerow(row)

def read_orders(header=False):
    orders = []
    with open(os.path.join(app.root_path, 'static', 'orders.csv')) as f:
        order_reader = csv.reader(f)
        for each in order_reader:
            orders.append(each)
    return orders if header else orders[1:]

def write_orders(orders):
    with open(os.path.join(app.root_path, 'static', 'orders.csv'), mode="w", newline="") as f:
        writer = csv.writer(f)
        for row in orders:
            writer.writerow(row)


'''
Index - Needs some updates.
'''
@app.route('/')
def index():
    return render_template('home.html', products=read_products())


'''
Individual product pages.

Needs adding to!
'''
@app.route("/product/<int:id>")
def product(id):
    products = read_products()
    selected = None
    for product in products:
        try:
            product_id = int(product[0])
        except (ValueError, IndexError):
            continue
        if product_id == id:
            selected = product
            break
    if not selected:
        return f"Product {id} not found."
    return render_template("product.html", product=selected)


'''
Order - needs adding to!
'''
@app.route("/order/<int:id>")
def order(id):
    products = read_products(header=True)
    header = products[0]
    rows = products[1:]

    selected_index = None
    for i, product in enumerate(rows):
        try:
            product_id = int(product[0])
        except (ValueError, IndexError):
            continue
        if product_id == id:
            selected_index = i
            break

    if selected_index is None:
        return f"Product {id} not found."

    selected = rows[selected_index]
    try:
        stock = int(selected[3])
    except (ValueError, IndexError):
        stock = 0

    if stock <= 0:
        return "Out of stock."

    selected[3] = str(stock - 1)
    write_products([header] + rows)

    orders = read_orders(header=True)
    order_rows = orders[1:]
    next_id = 1
    if order_rows:
        try:
            next_id = int(order_rows[-1][0]) + 1
        except (ValueError, IndexError):
            next_id = len(order_rows) + 1
    order_rows.append([str(next_id), selected[1], datetime.datetime.now().isoformat()])
    write_orders([orders[0]] + order_rows)

    return redirect(url_for("product", id=id))

@app.route("/orders")
def orders():
    return render_template("orders.html", orders=read_orders())



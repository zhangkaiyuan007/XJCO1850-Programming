from flask import flash, redirect, render_template, request, url_for
from app import app
import csv
import os

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


'''
Index - Needs some updates.
'''
@app.route('/')
def index():
    return render_template('home.html', products=read_products()[0])


'''
Individual product pages.

Needs adding to!
'''
@app.route("/product/<int:id>")
def product(id):
    return f"product {id}"


'''
Order - needs adding to!
'''
@app.route("/order/<int:id>")
def order(id):
    return f"order product no. {id}"



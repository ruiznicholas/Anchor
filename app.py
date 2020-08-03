# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import calc_charges
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about', methods=['GET','POST'])
def about():
    if request.method == 'POST':
        return render_template('about.html')
    else:
        return render_template('about.html')
@app.route('/products', methods=['GET','POST'])
def products():
    if request.method == 'POST':
        return render_template('products.html')
    else:
        return render_template('products.html')
@app.route('/checkout', methods=['GET','POST'])
def faq():
    if request.method == 'POST':
        return render_template('checkout.html')
    else:
        return render_template('checkout.html')

@app.route('/charges', methods=['GET','POST'])
def charges():
    if request.method == 'POST':
        num_products = request.form['num_products']
        product_cost = calc_charges(num_products)
        return render_template('charges.html', product_cost=product_cost)
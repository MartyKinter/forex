from flask import Flask, request, render_template, redirect, flash
import requests
from forex import get_symbols, is_valid_currency_code
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def forex_homepage():
    """Display page for entering values to convert"""
    symbol_data = get_symbols()
    
    return render_template("index.html", symbol_data=symbol_data)


@app.route("/result", methods=["POST"])
def process_form_data():
    """Process the form data and redirect to the results page"""
    conv_from = request.form["convert-from"]
    conv_to = request.form['convert-to']
    amount = request.form['amount']

    symbol_data = get_symbols()
    currency_codes = list(symbol_data['symbols'].keys())

    if not amount.isdigit():
        flash("Not a valid amount. (Amount must be an integer)")
        return redirect("/")

    if not is_valid_currency_code(conv_from, currency_codes) or not is_valid_currency_code(conv_to, currency_codes):
        return redirect("/")

    return redirect(f"/result?conv_from={conv_from}&conv_to={conv_to}&amount={amount}")
    

@app.route("/result")
def show_result():
    """Display the converted result"""
    conv_from = request.args.get("conv_from")
    conv_to = request.args.get("conv_to")
    amount = request.args.get("amount")

    url = f"https://api.exchangerate.host/convert?from={conv_from}&to={conv_to}&amount={amount}&places=2"
    response = requests.get(url)
    data = response.json()

    return render_template("result.html", data=data)


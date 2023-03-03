import requests
from flask import flash 

def is_valid_currency_code(code, currency_codes):
    if code not in currency_codes:
        flash(f"Not a valid code: {code}")
        return False
    else:
        return True

def get_symbols():
    symbol_url = 'https://api.exchangerate.host/symbols'
    symbol_response = requests.get(symbol_url)
    return symbol_response.json()   
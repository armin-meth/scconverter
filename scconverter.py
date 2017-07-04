#! /usr/bin/env python
import argparse
import urllib2
import json

class SimpleCurrencyConverter:
    def __init__(self, amount, from_currency, to_currency):
        self.check_args(amount, from_currency, to_currency)
        self.do_conversion(amount, from_currency, to_currency)

    def check_args(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            print "{} {} = {} {}".format(amount, from_currency, amount, to_currency)
            quit()
               
    def do_conversion(self, amount, from_currency, to_currency):
        print self.generate_output(amount, from_currency, to_currency)

    def generate_output(self, amount, from_currency, to_currency):
        return "{} {} = {} {}".format(amount, from_currency, float(self.get_from_to_rate(from_currency, to_currency)) * float(amount), to_currency)

    def get_from_to_rate(self, from_currency, to_currency):
        return self.list_rates(from_currency)[to_currency]

    def list_rates(self, from_currency):
        data = (self.get_data(from_currency))['rates']
        rates = {}
        {self.get_rates(key, value, rates) for (key, value) in data.items()}
        return rates

    def get_data(self, base):
        return json.loads(urllib2.urlopen("https://api.fixer.io/latest?base=" + base).read())
        
    def get_rates(self, key, value, rates):
        rates[key] = value

if __name__ == "__main__":
    currencies = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
    parser = argparse.ArgumentParser('scconverted')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('amount', type=float, default='1', const='1', nargs='?', help='Float value to calculate')
    parser.add_argument('fromcurrency', type=str.upper, default='EUR', const='EUR', nargs='?', choices=currencies, help='Convert from this currency')
    parser.add_argument('tocurrency', type=str.upper, default='USD', const='USD', nargs='?', choices=currencies, help='Convert to this currency')
    SimpleCurrencyConverter(parser.parse_args().amount, parser.parse_args().fromcurrency, parser.parse_args().tocurrency)
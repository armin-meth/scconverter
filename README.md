# scconverter
Simple Currency Converter

## Usage

    ./scconverter.py [-h] [-v] [amount] [from currency] [to currency]

## Arguments

- `-h` - show help message
- `-v` - show version number
- `amount` - amount of money to change, accept floats
- `from currency` - currency to convert from
- `to currency` - currency to convert to

## Supported currencies

AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HRK, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PLN, RON, 
RUB, SEK, SGD, THB, TRY, USD, ZAR

## Example

    # ./scconverter.py 5 EUR USD
    5.0 EUR = 5.6765 USD

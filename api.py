# coding: utf-8
import requests
import json
import datetime


class current:
    USD = 'USD'
    IDR = 'IDR'
    BGN = 'BGN'
    ILS = 'ILS'
    GBP = 'GBP'
    DKK = 'DKK'
    CAD = 'CAD'
    JPY = 'JPY'
    HUF = 'HUF'
    RON = 'RON'
    MYR = 'MYR'
    SEK = 'SEK'
    SGD = 'SGD'
    HKD = 'HKD'
    AUD = 'AUD'
    CHF = 'CHF'
    KRW = 'KRW'
    CNY = 'CNY'
    TRY = 'TRY'
    HRK = 'HRK'
    NZD = 'NZD'
    THB = 'THB'
    EUR = 'EUR'
    NOK = 'NOK'
    RUB = 'RUB'
    INR = 'INR'
    MXN = 'MXN'
    CZK = 'CZK'
    BRL = 'BRL'
    PLN = 'PLN'
    PHP = 'PHP'
    ZAR = 'ZAR'


def get_exchange_rates(base, symbols, date='latest'):
    if isinstance(date, datetime.date):
        date = date.strftime("%Y-%m-%d")
    api_url = 'http://api.fixer.io/{date}?base={base}&symbols={symbols}' \
        .format(base=base, symbols=','.join(symbols), date=date)
    r = requests.get(api_url)
    response = json.loads(r.content)
    return response


def get_one(current_one, current_two, *args, **kwargs):
    return get_exchange_rates(current_one, [current_two], *args, **kwargs)['rates'][current_two]


def eur_usd(*args, **kwargs):
    return get_one(current.EUR, current.USD, *args, **kwargs)

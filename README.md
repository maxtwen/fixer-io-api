Examples of usage:
   
    >>> get_exchange_rates(current.USD, [current.EUR, current.RUB], datetime.date(2006, 12, 29))
    {u'date': u'2006-12-29', u'base': u'USD', u'rates': {u'RUB': 26.333, u'EUR': 0.7593}}

    >>>> get_one(current.USD, current.EUR, datetime.date(2000, 01, 03))
    0.99108

    >>> eur_usd(datetime.date(2000, 01, 03))
    1.009
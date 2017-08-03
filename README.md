======================
bitfinex-python-client
======================

Python package to communicate with the bitfinex.net API.

Tested with Python 2.7+


Overview
========

There are two classes. One for the public part of API and a second for the
trading part.

Public class doesn't need user credentials, because API commands which this
class implements are not bound to bitfinex user account.

Description of API: https://www.bitfinex.com/pages/api

Requirements
============

It uses python package "requests" to send HTTP requests. As this package is not a built in module, you will have to get it with one of the following options:

1.  pip install requests

2.  C:\Python27\Scripts\easy_install.exe requests

3.  Or you can even place a proper "requests" folder next to your python code, one can be downloaded from here: https://pypi.python.org/pypi/requests/


Install
=======

Install from git::

    pip install git+git://github.com/streblo/bitfinex-python-client.git


Usage
=====

Here's a quick example of usage::

```
import bitfinex.client

public_client = bitfinex.client.Public()
print("Last bitcoin price on Bitfinex is " + str(public_client.get_last()) + " USD.")

lendbook = public_client.lendbook(limit_bids=0, limit_asks=5, currency='btc')
print ("\nFirst offers from lending book:")
for ask in lendbook['asks']:
	print (ask['amount'] + " BTC available at " + ask['rate'] + "% for " + str(ask['period']) + " days.")

trading_client = bitfinex.client.Trading(key='xxx', secret='xxx')
balances = trading_client.balances()
print ("\nYour balances at Bitfinex:")
for balance in balances:
	if float(balance['amount']) > 0.0:
		print ("You have " + balance['amount'] + " " + balance['currency'] + " in your " + balance['type'] + " account.")
```

How to activate a new API key
=============================

Get the API key from the website: https://www.bitfinex.com/account/api

import bitfinex.client
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
bitfinex_key = str(config['bitfinex']['key'])
bitfinex_secret = str(config['bitfinex']['secret'])

public_client = bitfinex.client.Public()
#print("Last bitcoin price on Bitfinex is " + str(public_client.get_last()) + " USD.")

trading_client = bitfinex.client.Trading(key=bitfinex_key, secret=bitfinex_secret)

balances = trading_client.balances()
positions = trading_client.positions()

total = 0
for balance in balances:
    amount = float(balance['amount'])
    if amount > 0.0:
        if balance['currency'] != "usd":
            ticker = public_client.ticker(balance['currency']+"usd")
            rate = ticker['bid']
        else:
            rate = "1"

        onebal = int(round(float(rate) * amount, 0))
        if balance['type'] == "trading":
            balance['type'] = "exchange"
        print (balance['type']
               + " " + balance['currency']
               + " " + str(round(amount, 2))
               + " x " + rate
               + " = " + str(onebal))

        total = total + onebal

print ("Balance: " + str(total))

print ("---")

pl = 0
for position in positions:

    tickerbuyccy = position['symbol'][:3]
    tickersellccy = position['symbol'][-3:]
    if tickersellccy != "usd":
        rate = float(public_client.ticker(tickersellccy+"usd")['bid']);
    else:
        rate = 1;
    #print ("symbol "+position['symbol']+", tb "+tickerbuyccy+" ts "+tickersellccy+" rate "+rate)

    onepl = int(float(position['pl']) * rate)

    roundcoef = 4
    if float(position['base']) > 1: roundcoef = 2
    if float(position['base']) > 1000: roundcoef = 0
    
    print ("margin " + position['symbol']
           + " (" + str(
           round(float(public_client.ticker(position['symbol'])['bid']), 4)
           ) + ") "
           + str(round(float(position['amount']), 2))
           + " @ " + str(round(float(position['base']), roundcoef))
           + " = " + str(onepl))

    pl = pl + onepl

print ("PL: " + str(pl))

print ("---")

total = total + pl
print ("Total: " + str(total))

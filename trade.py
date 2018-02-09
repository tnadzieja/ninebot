#get the system
import sys, signal, time
from bittrex import bittrex

#API details
key  = 'KEY'
secret = 'SECRET'


api = bittrex(key, secret)

#goodbye~
def sigint_handler(signum, frame):
    print '\n[!] Escaped! Goodbye<3'
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)


coin = sys.argv[1]
btcBalance = float(sys.argv[2])
percentage_tp = float(sys.argv[3])
percentage_sl = float(sys.argv[4])


coinPrice = api.getticker("BTC-" + coin)
buyPrice = coinPrice['Ask']
numCoins = btcBalance / buyPrice
api.buylimit('BTC-' + coin, numCoins, buyPrice)


tp = buyPrice + ((percentage_tp/100) * buyPrice)
print '\n[+] Stake set to {} BTC'.format(tp)
sl = buyPrice - ((percentage_sl/100) * buyPrice)
print '\n[+] Stop Loss set to {} BTC'.format(sl)
i=0
while True:
    price = api.getticker("BTC-" + coin)
    last = price['Last']
    print '\n {} Current Price: {} BTC'.format(i, last)
    if last >= tp:
        print '\nTarget reached!'
        api.selllimit('BTC-' + coin, numCoins, tp)
        break
    elif last <= sl:
        print '\nStop Loss taken.'
        api.selllimit('BTC-' + coin, numCoins, sl)
        break
    i = i+1
    time.sleep(2)

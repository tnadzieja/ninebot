Login Phase
-----------------
create bittrex library (+)

login via RESTful API (+)

gather current price data based on specific(?) markets (+)

gather historical price data based on specific(?) markets (+)


Determine Trade
-----------------
Moving average convergence divergence(python pandas module)

Relative strength Index

Determine buy order based on 'x' timed 'sticks'

Pay attention to the 'overall market' strength


Buy/Sell Orders
-----------------
activate a buy/sell order (+)

remove buy/sell order if not fulfilled within 10 seconds

adjust 'purchased' amount depending on fulfilled Orders


Stop Loss / Trailing Stop
-----------------
sell (if) xx% is lost on a sale (+)

determine when the 'right' time to sell is
 - if red, wait for xx% turn
 - if green, wait for xx% flip


Output
-----------------
create a table to log transactions (date, time, order fulfilled)

create an interface to view all transactions

have a ruly "total earned versus total lost"

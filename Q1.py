import numpy as np
import random
import sys


def gen(frac, N):

    vec = [i+1 for i in range(N)]
    vec = list(np.random.permutation(vec))
    # vec = [7, 4, 6, 2, 3, 8, 1, 5]
    outvec = [i for i in vec]

    while len(vec) * frac >= 1:
        cnt = int(len(vec) * frac)
        outvec = outvec + vec[:cnt]
        vec = vec[:cnt]
        # print outvec,vec
    return outvec


def generateTrade(N, symbols):

    last = {}
    res = []
    for time in range(N):
        symbol = random.choice(symbols)
        quant = random.randint(100,10000)
        
        lower = 50
        upper = 500
        
        if symbol in last:
            lower = max(last[symbol] - 5, 50)
            upper = min(last[symbol] + 5,500)
        price = random.randint(lower,upper)
        while symbol in last and price==last[symbol]:
            price = random.randint(lower,upper)
        
        # if not (lower==50 and upper==500):
        #     print symbol,last[symbol],price
        last[symbol] = price
        res += [[time,symbol,quant,price]]

        if time % 100000 == 0:
            print "Processed:",time,'          \r',
            sys.stdout.flush()
    print "Trade Data Generated!          "
    return res


def dumpTrade(trade):
    f = open('trade.txt','w')
    f.write('Time,Symbol,Quantity,Price\n')
    f.write("\n".join(map(lambda x: ",".join(map(str,x)), trade)))
    f.close()




sym = gen(0.3,70002)

trade = generateTrade(10000000, sym)

dumpTrade(trade)



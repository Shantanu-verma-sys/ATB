from webdata import *


def on_data(m):
    '''Main algo here'''
    print(m)
    
if __name__ == "__main__":

    interval = '4h'
    coin_name = 'btc'
    coin_vs_name = 'usdt'
    coin_pair = coin_name + coin_vs_name
    
    F = FetchData(interval,coin_pair,on_data)

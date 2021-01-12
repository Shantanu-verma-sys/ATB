import json
import websocket

time_interval = "4h"

def onopen(con):
    print("connection open")
    x = json.dumps({
      "method": "SUBSCRIBE",
      "params": [
        "btcusdt@kline_"+time_interval,
      ],
      "id": 1
    })
    con.send(x)

def onErr(con,err):
    print(err)

def onMes(con,m):
    val = json.loads(m)["data"]
    p = {"s":"Symbol ",
         "i":"Interval ",
         "o":"Open Price ",
         "c":"Close Price ",
         "h":"High Price ",
         "l":"Low Price ",
         "x":"Closed? "
         }
    
    for i in val["k"]:
        if i in p:
            print(p[i]+" : "+str(val["k"][i]))
    print("-"*20)
        

def onClose(con):
    print("con closed")

con = websocket.WebSocketApp("wss://stream.binance.com:9443/stream?streams=kline_"+time_interval,on_message = onMes,on_error = onErr,on_close = onClose)
con.on_open = onopen
con.run_forever()

import json
import websocket

class FetchData:
    def __init__(self,interval,coin,clb):
        self.inter = interval
        self.coin = coin
        self.mapping = {"s":"Symbol ",
         "i":"Interval ",
         "o":"Open Price ",
         "c":"Close Price ",
         "h":"High Price ",
         "l":"Low Price ",
         "x":"Closed? "
         }
        self.jsonData = {
          "method": "SUBSCRIBE",
          "params": [
            coin+"@kline_"+interval,
          ],
          "id": 1
        }
        self.url = "wss://stream.binance.com:9443/stream?streams=kline_"+interval
        self.connection = websocket.WebSocketApp(self.url,
                                                    on_message = lambda ws,msg: self.onMes(ws, msg),
                                                    on_error   = lambda ws,msg: self.onErr(ws, msg),
                                                    on_close   = lambda ws:     self.Close(ws),
                                                    on_open    = lambda ws:     self.onopen(ws))
        self.callbackMessage = clb
        self.connection.run_forever()
        
    def onopen(self,con):
        print("connection open")
        x = json.dumps(self.jsonData)
        con.send(x)

    def onErr(self,con,err):
        print(err)

    def onMes(self,con,m):
        self.callbackMessage(m)    

    def onClose(self,con):
        print("con closed")

import websocket
import json


ws = websocket.WebSocket()
ws.connect("wss://ws.lightstream.bitflyer.com/json-rpc", http_proxy_host="127.0.0.1", http_proxy_port=1080)

ws.send("{\"method\":\"subscribe\",\"id\":1533521924059,\"params\":{\"channel\":\"lightning_ticker_ETH_BTC\"}}")

while True:
    result = ws.recv()
    d = json.loads(result)


    #print("Received:[%s]" % d['trade_volume'])
    print("Received:[%s]" % result)
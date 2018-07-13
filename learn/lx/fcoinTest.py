import fcoin

fcoin_ws = fcoin.init_ws()
topics = ["ticker.ethbtc", "ticker.btcusdt"]
# fcoin_ws.handle(print)
fcoin_ws.sub(topics)
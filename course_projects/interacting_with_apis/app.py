import time
from libraries.openexchange import OpenExchangeClient

APP_ID = "75869b60a9da49c693b61e277bebdcd9"
client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
exchange_amt = client.convert(usd_amount, "USD", "INR")
print(f"Time taken: {time.time() - start}")

usd_amount = 1000
start = time.time()
exchange_amt = client.convert(usd_amount, "USD", "INR")
print(f"Time taken: {time.time() - start}")

usd_amount = 1000
start = time.time()
exchange_amt = client.convert(usd_amount, "USD", "INR")
print(f"Time taken: {time.time() - start}")

usd_amount = 1000
start = time.time()
exchange_amt = client.convert(usd_amount, "USD", "INR")
print(f"Time taken: {time.time() - start}")

print(f"USD{usd_amount} is INR{exchange_amt:.2f}")
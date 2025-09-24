import requests
import sys

def get_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data.get(coin, {}).get("usd")
    return None

if __name__ == "__main__":
    coin = sys.argv[1] if len(sys.argv) > 1 else "bitcoin"
    price = get_price(coin)
    if price:
        print(f"{coin.capitalize()} price: ${price}")
    else:
        print("Error fetching price.")

import requests
from itertools import cycle

proxy_list = [
    "http://proxy1:8080",
    "http://proxy2:8080",
    "http://proxy3:8080"
]
proxy_pool = cycle(proxy_list)
MAX_REQUESTS_PER_PROXY = 10

requests_count = {proxy: 0 for proxy in proxy_list}

url = "https://api.example.com/endpoint"

for i in range(50):  
    proxy = next(proxy_pool)
    if requests_count[proxy] < MAX_REQUESTS_PER_PROXY:
        try:
            print(f"Using proxy {proxy} for request {i + 1}.")
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
            response.raise_for_status()
            print(f"Response: {response.status_code} - {response.text}")
            requests_count[proxy] += 1
        except requests.RequestException as e:
            print(f"Proxy {proxy} failed: {e}")

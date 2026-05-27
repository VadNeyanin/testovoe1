import requests

def request(URL, code):
    r = requests.get(f"{URL}{code}", timeout=10)
    return r.status_code, r.text
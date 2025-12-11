import requests
from time import sleep

def test_ping_service():
    for _ in range(3):
        resp = requests.get("https://httpbin.org/get")
        if resp.status_code == 200:
            break
        sleep(1)  # wait a second and retry
    assert resp.status_code == 200

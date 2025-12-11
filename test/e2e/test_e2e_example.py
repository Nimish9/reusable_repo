import requests

def test_ping_service():
    resp = requests.get("https://httpbin.org/get")
    assert resp.status_code == 200
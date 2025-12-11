# test/e2e/test_e2e_example.py
import requests

def test_ping_service(mocker):
    # Create a fake response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "ok"}

    # Patch requests.get to return the fake response
    mocker.patch("requests.get", return_value=mock_response)

    # Your code calls requests.get, but it will use the fake response
    resp = requests.get("https://httpbin.org/get")
    
    assert resp.status_code == 200
    assert resp.json() == {"message": "ok"}

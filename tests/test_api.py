import requests

BASE_URL = "http://127.0.0.1:5000"

def test_server_running():
    import requests
    res = requests.get("http://127.0.0.1:5000/read_did?did=0xF190")
    assert res.status_code == 200

# Positive test
def test_session_valid():
    res = requests.post(
        f"{BASE_URL}/session",
        json={"request": "0x10"}
    )
    assert res.status_code == 200
    assert res.json()["response"] == "0x50"


#  Negative test (invalid request)
def test_session_invalid():
    res = requests.post(
        f"{BASE_URL}/session",
        json={"request": "0x99"}
    )
    assert res.status_code == 200
    assert res.json()["response"] == "0x7F"


#  Missing field
def test_session_missing_field():
    res = requests.post(f"{BASE_URL}/session", json={})
    assert res.status_code == 400


# Read DID positive
def test_read_did_valid():
    res = requests.get(
        "http://127.0.0.1:5000/read_did",
        params={"did": "0xF190"}
    )
    assert res.status_code == 200
    assert res.json()["response"] == "VIN123456789"


#  Invalid DID
def test_read_did_invalid():
    res = requests.get(
        f"{BASE_URL}/read_did",
        params={"did": "0x0000"}   # ✅ correct
    )
    assert res.status_code == 200
    assert res.json()["response"] == "NOT_FOUND"


#  Missing DID
def test_read_did_missing():
    res = requests.get(f"{BASE_URL}/read_did")
    assert res.status_code == 400
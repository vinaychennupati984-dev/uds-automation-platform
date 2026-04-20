from uds.uds_handler import UDSHandler
import requests

def test_session_control():
    uds = UDSHandler()
    assert uds.session_control("0x10") == "0x50"

def test_read_did():
    uds = UDSHandler()
    assert uds.read_did("0xF190") == "VIN123456789"

def test_invalid_session():
    uds = UDSHandler()
    assert uds.session_control("0x99") == "0x7F"

def test_api_session():
    res = requests.post("http://127.0.0.1:5000/session",
                        json={"request": "0x10"})
    assert res.json()["response"] == "0x50"
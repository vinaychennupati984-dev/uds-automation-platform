from uds.uds_handler import UDSHandler

def run():
    uds = UDSHandler()

    print("Session Control:", uds.session_control("0x10"))
    print("Read DID:", uds.read_did("0xF190"))

if __name__ == "__main__":
    run()
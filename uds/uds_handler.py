import logging

logging.basicConfig(
    filename='test.log',
    filemode="w",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class UDSHandler:

    def session_control(self, request):
        logging.info(f"Session request received: {request}")

        if request == "0x10":
            logging.info("Positive response")
            return "0x50"

        logging.warning("Invalid session request")
        return "0x7F"

    def read_did(self, did):
        logging.info(f"Read DID request: {did}")

        if did == "0xF190":
            return "VIN123456789"

        logging.warning("DID not found")
        return "NOT_FOUND"
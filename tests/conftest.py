import subprocess
import time
import pytest
import sys
import logging

logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="session", autouse=True)
def start_api_server():
    logging.info("Starting API server...")

    process = subprocess.Popen(
        [sys.executable, "-m", "api.server"]
    )

    time.sleep(5)

    yield

    logging.info("Stopping API server...")
    process.terminate()
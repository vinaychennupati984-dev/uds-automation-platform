# UDS Automation Platform 🚗
This project demonstrates an end-to-end automotive diagnostic automation framework built using Python. It simulates real-world vehicle communication by integrating UDS (Unified Diagnostic Services) with a REST API layer, automated testing using pytest, and CI/CD execution using Jenkins.

The system mimics how backend services interact with vehicle ECUs in modern automotive architectures, including API-triggered diagnostics and automated validation workflows.

## Overview

This project simulates an automotive diagnostic system integrating:

* UDS (Unified Diagnostic Services)
* REST API (Flask)
* Automated Testing (Pytest)
* CI/CD (Jenkins)

## Architecture

pytest → API (Flask) → UDS Handler

## Features

* UDS Session Control
* Read DID (VIN simulation)
* API-based diagnostics
* Automated test execution
* Auto API start/stop using pytest fixtures
* JUnit XML & HTML reporting

## Tech Stack

* Python
* Flask
* Pytest
* Jenkins

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run tests (API auto-starts)

pytest

### 3. Generate reports

pytest --junitxml=report.xml --html=report.html

## CI/CD

* Jenkins pipeline included (Jenkinsfile)
* Automated test execution on code changes

## Author

Vinay Chandra

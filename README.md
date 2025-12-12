# Flask Contracts Lab

## Overview
This lab builds on foundational Flask routing concepts by introducing
status codes and conditional responses based on in-memory data.  
The focus is on returning appropriate HTTP responses and validating behavior
using pytest.

---

## Project Structure

flask-contracts-lab/
flask-contracts-lab/server/
flask-contracts-lab/server/app.py
flask-contracts-lab/server/testing/
flask-contracts-lab/server/testing/app_test.py
flask-contracts-lab/server/testing/conftest.py
flask-contracts-lab/pytest.ini
flask-contracts-lab/README.md


- server/app.py contains the Flask application and route logic
- server/testing/app_test.py holds automated tests for each route
- pytest.ini configures pytest to correctly locate application modules

## Application Overview
The Flask app provides two routes:

/contract/<id>
- Accepts a dynamic integer representing a contract ID.
- If the contract exists, returns the associated contract information.
- If the contract does not exist, returns a 404 Not Found response.

/customer/<customer_name>
- Accepts a dynamic string representing a customer name.
- If the customer exists, returns a 204 No Content response.
- If the customer does not exist, returns a 404 Not Found response.

- Responses are returned as plain text or empty bodies to simplify testing
  and focus on HTTP status code behavior.

## Key Features
- Dynamic route handling with type converters
- Conditional responses based on in-memory data
- Proper use of HTTP status codes (200, 204, 404)
- Automated testing using Flask’s test client and pytest

## Running the Tests

From the project root use the following:
- python -m pytest

## General project notes

Project passed through ChatGPT to identify syntax issues, clarify routing
behavior, and assist in drafting this README.md file. The README.md was
reviewed and edited for clarity, consistency, and alignment with lab
requirements prior to submission.

#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/12/25
# Version: 1.1

"""
Flask application for managing simple contract and customer lookups.

The app exposes two routes:
- /contract/<id>: returns contract information for a valid contract ID
- /customer/<customer_name>: confirms a customer exists using a 204 response

The application uses in-memory data structures and returns plain text
responses to support automated testing with pytest.
"""

from flask import Flask, request, current_app, g, make_response

# In-memory contract data provided by the lab
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

# In-memory list of valid customers
customers = ["bob", "bill", "john", "sarah"]

# Create the Flask application instance
app = Flask(__name__)


@app.route("/contract/<int:id>")
def contract(id):
    """Handle requests for a specific contract by ID."""
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"]

    return "", 404


@app.route("/customer/<string:customer_name>")
def customer(customer_name):
    """Confirm whether a customer exists using a 204 response."""
    if customer_name in customers:
        return make_response("", 204)

    return "", 404


if __name__ == '__main__':
    # Run the app locally for development and debugging
    app.run(port=5555, debug=True)

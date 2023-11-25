# TG-BOT

Architecture Overview:
Lambda Function - lambda_function.py:

This Lambda function is responsible for handling incoming Telegram commands, specifically the "/start" command.
It uses the telegram library to interact with the Telegram Bot API for sending messages.
The start function:
Parses the incoming Telegram event from the API Gateway.
Calls the moralis.get_prices() function to fetch real-time Ethereum token prices.
Formats the data and sends a response back to the Telegram user.
Lambda Function - moralis.py:

This Lambda function is responsible for making requests to the Moralis API to retrieve Ethereum token prices.

The get_prices function:

Sends a POST request to the Moralis API endpoint, providing Ethereum token addresses and exchange information.
Handles errors such as HTTP request failures, JSON decoding errors, and unexpected exceptions.
Parses and extracts relevant information from the Moralis API response.
Returns the formatted data to the calling function.



1. Lambda Function - lambda_function.py:
Description:

The lambda_function.py Lambda function handles Telegram commands and fetches real-time Ethereum token prices.
Configuration:

Environment Variables:
TG_BOT_API_KEY: Your Telegram Bot API key.
(Additional configuration if needed)
Dependencies:

Python Libraries:
telegram

Usage:

The function is triggered by the "/start" command from the Telegram user.
Upon receiving the command, it fetches real-time Ethereum token prices using moralis.get_prices().

2. Lambda Function - moralis.py:
Description:

The moralis.py Lambda function interacts with the Moralis API to fetch real-time Ethereum token prices.

Configuration:

Environment Variables:
MORALIS_API_KEY: Your Moralis API key.

Dependencies:

Python Libraries:
requests
Usage:

The function is called by lambda_function.py to fetch Ethereum token prices.
It sends a POST request to the Moralis API, processes the response, and returns formatted data.

Deployment:
Deploy both Lambda functions to your AWS Lambda environment.
Set up an API Gateway to expose an HTTP endpoint for the lambda_function.py.
Configure the Telegram Bot with the provided TG_BOT_API_KEY.
Ensure that the Moralis API key (MORALIS_API_KEY) is correctly configured in the Lambda environment.

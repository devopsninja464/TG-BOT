# TG-BOT

# Architecture Overview:

![TG_bOT_Serverless_Architecture](https://github.com/devopsninja464/TG-BOT/assets/77762256/0932685a-5eed-483a-8c95-f7ccb50e0ba1)


## Lambda Function - lambda_function.py:

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

# Deployment:

Deploy both Lambda functions to your AWS Lambda environment.
Set up an API Gateway to expose an HTTP endpoint for the lambda_function.py.
Configure the Telegram Bot with the provided TG_BOT_API_KEY.
Ensure that the Moralis API key (MORALIS_API_KEY) is correctly configured in the Lambda environment.

=================================================================================================

another lambda function to set the webhook and runs for every 5min to make the requests active. 

# Webhook Setup Lambda Function

This AWS Lambda function is designed to automate the process of setting up a webhook for a Telegram bot using the Telegram Bot API. The function is triggered by an event, and it performs the necessary steps to configure the webhook URL through the Telegram API.

Lambda Function - webhook_setup.py

Description:

The webhook_setup.py Lambda function automates the process of setting up a webhook for a Telegram bot.
Configuration:

Environment Variables:
TG_BOT_API_KEY: Your Telegram Bot API key.
APIGateway_URL: The URL of your API Gateway endpoint.

Dependencies:

Python Libraries:
os
json
requests
Usage:

Event Trigger:

The Lambda function is triggered by an event, typically through an AWS CloudWatch Events rule or another event source.
Ensure that the necessary permissions and triggers are set up to invoke the Lambda function.

Webhook Setup:

The function fetches the Telegram Bot API key and API Gateway URL from environment variables.
Constructs the Telegram Bot API endpoint URL with the provided parameters.
Sends a POST request to the Telegram Bot API to set up the webhook with the specified URL.

Error Handling:

The function includes error handling to manage potential issues during the webhook setup process.
If the HTTP request to the Telegram API fails, the function catches the requests.exceptions.RequestException and logs the error.
For other unexpected exceptions, a general Exception block captures and logs the error.

# Deployment:

Environment Setup:

Configure the necessary environment variables (TG_BOT_API_KEY and APIGateway_URL) in the AWS Lambda console.
Deploy Lambda Function:

Deploy the lambda_function_tg_webhook.py Lambda function to your AWS Lambda environment.
Set Up Triggers:

Configure event triggers for the Lambda function, such as AWS CloudWatch Events, to execute the function at scheduled intervals or specific events.


import os
import json
import requests

def lambda_handler(event, context):
    try:
        bot_token = os.environ.get('TG_BOT_API_KEY')
        api_gateway_url = os.environ.get('APIGateway_URL')
 
        api_url = f'https://api.telegram.org/bot{bot_token}/setWebhook?url={api_gateway_url}'
        response = requests.post(api_url)

        # Check if the response status code is in the range [200, 299]
        response.raise_for_status()

        print("Webhook set up successfully.")
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"Failed to set up webhook. Error: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

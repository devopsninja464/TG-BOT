import os
import requests
import json

def get_prices():
    try:
        url = "https://deep-index.moralis.io/api/v2.2/erc20/prices?chain=eth&include=percent_change"
        api_key = os.environ.get('MORALIS_API_KEY')
        payload = {
            "tokens": [
                {
                    "token_address": "0xxxxxxx",
                    "exchange": "uniswapv3"
                },
                {
                    "token_address": "0xxxxxxx",
                    "exchange": "uniswapv2"
                },
                {
                    "token_address": "0xxxxxxx",
                    "exchange": "uniswapv2"
                }
            ]
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-Key": api_key
        }

        response = requests.post(url, json=payload, headers=headers)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON data
        response_data = response.json()

        # Specify the keys you want to print
        keys_to_print = ["tokenName", "tokenAddress", "usdPrice", "24hrPercentChange"]

        # Create a list to store data
        data = []

        # Iterate through each dictionary in the list
        for entry in response_data:
            coin_data = {}
            for key in keys_to_print:
                coin_data[key] = entry.get(key)
            data.append(coin_data)

        # Print or return the data as needed
        # print(data)
        return data

    except requests.exceptions.RequestException as req_ex:
        print(f"Error in making the HTTP request: {req_ex}")
    except json.JSONDecodeError as json_ex:
        print(f"Error decoding JSON response: {json_ex}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    get_prices()

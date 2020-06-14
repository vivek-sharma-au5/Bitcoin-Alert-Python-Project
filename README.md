# Bitcoin-Alert-Python-Project

A simple Bitcoin Alert python program which sends notifications of bitcoin price whenever the price goes under user provided threshold.

## Project Overview

- Program will send notifications on user selected platform.
- Four options for choice of platform(Telegram,Twitter,Email and SMS)
- User will receive updates after a user provided time interval.
- User has the option to select which type of currency he wants the price to be in.
- User has to select the Threshold below which he wants to receive the alerts.

## Build With

- [Python](https://www.python.org/)
- [Coin Market Cap API](https://coinmarketcap.com/api/)
- [IFTTT](https://ifttt.com/join)

## How to Run

Program can be started with or without parameters.For running the program according to user requirements user need to provide four parameters (currency,threshold,interval and platform)

- Running with default parameters.
  Results obtained using default parameter will have `USD` as currency, `10000` as threshold, `5`minutes as interval, `telegram` as platform.

```shell
$ python main.py

```

- Running with user provided parameters.
  Here User will need provide parameter in the manner described below.

```shell
$ python main.py INR 80000 1 Email

```

## Code Usage

- For Parsing Command line parameters

```python

import argparse

parser = argparse.ArgumentParser(description='Bitcoin Alert Help')

# Parsed command line arguments
# Currency argument with USD as default value
parser.add_argument('currency', nargs='?', type=str, default='USD',
                    help='Currency Code eg: USD ,INR')

# Limit argument with 10000$ as default value
parser.add_argument('limit', nargs='?', type=int, default=10000,
                    help='Price Limit eg: 1000')

# interval argument with 0.1 minutes as default value
parser.add_argument('interval', nargs='?', type=float, default=0.1,
                    help='Alert Interval(in minutes) eg:5')

# Platform argument with Telegram as default value
parser.add_argument('platform', nargs='?', type=str, default='telegram',
                    help='Destination(Platform where you want the notification) eg: Telegram,Twitter')
args = parser.parse_args()


```

- For getting bitcoin data from [Coin Market Cap API](https://coinmarketcap.com/api/).

```python
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# API url for fetching cryptocurrency data
bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# Parameters to get desired data from API
parameters = {
    'start': '1',
    'limit': '2',
    'convert': currency.upper()
}
# Header defining type of data and API key used to fetch data
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '915a0519-6536-4456-86e8-0e3522d695db',
}

session = Session()
session.headers.update(headers)


def get_latest_bitcoin_price():
    try:
        response = session.get(bitcoin_api_url, params=parameters)
        data = json.loads(response.text)
        return float(data["data"][0]['quote'][currency.upper()]['price'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

```

- For Sending data to [IFTTT](https://ifttt.com/join) webhooks and running required applets.

```python

import requests

# IFTTT URL connects to webhook
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/{}/with/key/dN1MNDT-EwdFPCUCa4UK7Q'


def post_to_ifttt_webhook(event, value, value2):

    # The payload that will be sent to IFTTT service
    data = {'value1': value, 'value2': value2}
    ifttt_event_url = ifttt_webhook_url.format(
        event)  # Inserts our desired event
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)


```

## Learnings

- How to obtain data from API and how to use python requests module.
- How to create IFTTT applets and use Webhooks and other platforms to receive notifications.
- Creating a python program with various different modules.
- Using argparse to parse command line parameters.

## Author

Vivek Sharma
[Bitcoin Alert Telegram Channel](https://t.me/bitcoin_live_alerts)

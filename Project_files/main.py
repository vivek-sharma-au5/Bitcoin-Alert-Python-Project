import sys
import time
from datetime import datetime
from get_data_from_api import get_latest_bitcoin_price, price_limit, currency, alert_interval, platform
from ifttt_notifications import post_to_ifttt_webhook
from time import sleep

# Price Threshold
limit = price_limit


def print_red(skk):
    # Prints red color text in console
    print("\033[91m {}\033[00m" .format(skk))


def print_green(skk):
    # Prints green color text in console
    print("\033[92m {}\033[00m" .format(skk))


def print_yellow(skk):
    # Prints yellow color text in console
    print("\033[93m {}\033[00m" .format(skk))


def print_cyan(skk):
    # Prints cyan color text in console
    print("\033[96m {}\033[00m" .format(skk))


def print_purple(skk):
    # Prints purple color text in console
    print("\033[94m {}\033[00m" .format(skk))


def bitcoin_server_interface():
    # Prints the server interface once the program is started
    print_green("""
              ₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿
            ₿₿                                       ₿₿
          ₿₿           Bitcoin Alert Service           ₿₿
            ₿₿                                       ₿₿
              ₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿
    """
                )
    print_cyan("""You can choose from variety of currencies for your alerts
            Try one of the following
        """)
    print_cyan(""" USD >>> US Dollars""")
    print_green(" INR >>> Indian Rupee")
    print_red(" EUR >>> Euros")
    print_yellow(" CNY >>> Chinese Yuan Renminbi")
    print_purple(" GBP >>> UK Pound Sterling")
    print(""" You will start getting notifications via """ + platform)


bitcoin_server_interface()


def main():
    alert_number = 0

    while True:
        # Prints Alert Data in console
        rate = get_latest_bitcoin_price()
        date = datetime.now()

        # Prints Current Rate
        print(" Current Rate "+"in " + currency.upper()+" ==>", end="")
        print_red("%.2f" % rate)

        # Prints alert date
        print(" Alert date ==>", end="")
        alert_date = datetime.now().strftime('%d.%m.%Y')
        print_yellow(alert_date)

        # Prints alert time
        alert_time = datetime.now().strftime('%H:%M:%S')
        print(" Alert time ==>", end="")
        print_cyan(alert_time)

        # Prints Alert number
        alert_number += 1
        print(" Alert number :", alert_number)
        print(" *********************************")

        # Send a alert in case rate is below limit
        # Sends Alert to telegram Channel
        if platform.lower() == 'telegram' and rate < limit:
            post_to_ifttt_webhook(
                'bitcoin_price_update_telegram', "%.2f" % rate, currency.upper())

        # Posts alert via tweet on twitter
        if platform.lower() == 'twitter' and rate < limit:
            post_to_ifttt_webhook(
                'bitcoin_price_update_twitter', "%.2f" % rate, currency.upper())

        # Sends Alert to mobile via SMS
        if platform.lower() == 'message' and rate < limit:
            post_to_ifttt_webhook(
                'bitcoin_price_update_message', "%.2f" % rate, currency.upper())

        # Sends Alert to email
        if platform.lower() == 'email' and rate < limit:
            post_to_ifttt_webhook(
                'bitcoin_price_update_email', "%.2f" % rate, currency.upper())

        # Sleep period between two notifications
        time.sleep(alert_interval * 60)


if __name__ == '__main__':
    main()

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

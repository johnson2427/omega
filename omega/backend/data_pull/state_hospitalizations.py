import requests
from requests.structures import CaseInsensitiveDict

url = "https://jhucoronavirus.azureedge.net/jhucoronavirus/hospitalization_by_state.json"

headers = CaseInsensitiveDict()
headers["authority"] = "jhucoronavirus.azureedge.net"
headers["sec-ch-ua"] = '"Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'
headers["sec-ch-ua-mobile"] = "?0"
headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
headers["accept"] = "*/*"
headers["origin"] = "https://coronavirus.jhu.edu"
headers["sec-fetch-site"] = "cross-site"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-dest"] = "empty"
headers["referer"] = "https://coronavirus.jhu.edu/"
headers["accept-language"] = "en-US,en;q=0.9"


resp = requests.get(url, headers=headers)

print(resp.status_code)


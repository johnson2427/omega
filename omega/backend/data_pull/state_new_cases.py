import requests
from requests.structures import CaseInsensitiveDict

url = "https://jhucoronavirus.azureedge.net/jhucoronavirus/testing/jh-covid-tool.v3.json"

headers = CaseInsensitiveDict()
headers["sec-ch-ua"] = '"Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'
headers["Referer"] = "https://coronavirus.jhu.edu/"
headers["sec-ch-ua-mobile"] = "?0"
headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"


resp = requests.get(url, headers=headers)

print(resp.status_code)


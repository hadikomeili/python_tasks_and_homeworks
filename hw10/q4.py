from bs4 import BeautifulSoup
import requests

url = "https://www.pcmag.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
p_list = soup.find_all("p")
with open('q4.txt', 'a') as f:
    for p in p_list:
        s = str(p) + '\n'
        f.write(s)
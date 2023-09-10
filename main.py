
import requests 

def fetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/topic/university/news"

fetchAndSaveToFile(url,"data/times.html")
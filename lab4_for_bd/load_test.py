import requests
import threading
import time

URL = "http://16.171.66.23:5000/health"

def spam():
    while True:
        try:
            requests.get(URL)
        except:
            pass

threads = []

for i in range(200):   
    t = threading.Thread(target=spam)
    t.start()
    threads.append(t)

print("Load started...")

import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import time
from config import url, interval_time

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)


def handle_found_appointments(num_found):
    # you can add your own handler (e.g. sounds, telegram) here
    print("Yeah! %d possible appointments" % num_found)

def crawl():
    html = requests.get(url)
    if(html.status_code != 200):
        print("Website Error")
        return
    soup = BeautifulSoup(html.text, 'html.parser')
    logging.info("Occupied: %d" % len(soup.find_all("td", { "class": "nichtbuchbar" })))
    found = len(soup.find_all("td", { "class": "buchbar" }))
    if found > 0:
        logging.info("FOUND %d POSSIBLE APPOINTMENTS!" % found)
        handle_found_appointments(found)


if url == "enter-url-here":
    logging.error("You have to enter a URL (get from Bürgeramt 'Termin Berlinweit suchen')")
    exit()

while True:
    crawl()
    time.sleep(interval_time)

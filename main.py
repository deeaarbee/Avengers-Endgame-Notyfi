import requests
from bs4 import BeautifulSoup
import time


while True:
    url = "https://in.bookmyshow.com/buytickets/avengers-endgame-chennai/movie-chen-ET00100559-MT/20190426"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    if str(soup).find("Luxe") == -1 or str(soup).find("SPI: S2 Theyagaraja - Thiruvanmiyur, Chennai") == -1:
        print("Not Found")
        time.sleep(10)
        continue

    else:
        import os
        os.system('say "Avengers Bookings open!!"')

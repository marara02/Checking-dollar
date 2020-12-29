import requests
from bs4 import BeautifulSoup
import time


class Currency:
    Dollar_KZ = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%B2+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&rlz=1C1GCEU_ruKZ929KZ929&oq=%D0%B4%D0%BE%D0%BB%D0%BB&aqs=chrome.1.69i57j0i433l6j46i433.5667j0j7&sourceid=chrome&ie=UTF-8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    current_converted_price = 0

    def __init__(self):
        self.current_converted_price = float(self.current_converted_price().replace(',','.'))

    def get_current_price(self):
        full_page = requests.get(self.Dollar_KZ, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.find_all("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(',','.'))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")

        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")

        print("Сейчас курс: 1 доллар = " + str(currency))
        time.sleep(3)  # Засыпание программы на 3 секунды
        self.check_currency()


currency = Currency()
currency.check_currency()

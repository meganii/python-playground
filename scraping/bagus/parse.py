import requests
from bs4 import BeautifulSoup
import urllib.parse
import json


def main():
    with open('gcc_ikebukuro_nishiguchi.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # t1 = soup.find_all('table')[0]
    for table in soup.find_all('table'):
        col1 = table.select_one('.col1').get_text()
        for tr in table.find_all('tr'):
            col2 = tr.select_one('.col2').get_text() if tr.select_one('.col2') is not None else ''
            col3 = tr.select_one('.col3').get_text() if tr.select_one('.col3') is not None else ''
            if (col2):
                print(col1 + " " + col2 + ':' + col3.strip())


if __name__ == "__main__":
    main()
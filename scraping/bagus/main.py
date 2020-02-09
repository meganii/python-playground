import requests
from bs4 import BeautifulSoup
import urllib.parse
import json

def main():
    url = 'https://www.bagus-99.com/shops/gcc_ikebukuro_nishiguchi/'
    response = requests.get(url)

    with open('gcc_ikebukuro_nishiguchi.html', 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    main()
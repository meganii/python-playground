"""
db stock
"""

import requests

def main():
    """
    main
    """
    ticker = '2928-S'
    url = "http://k-db.com/stocks/{0}?download=csv".format(ticker)
    request = requests.get(url)
    lines = request.text.splitlines()

    for line in lines:
        print(line)

    # file_name = "{0}.csv".format(ticker)
    # urllib.request.urlretrieve(url, file_name)

if __name__ == '__main__':
    main()

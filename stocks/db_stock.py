"""
db stock
"""

import urllib.request

def main():
    """
    main
    """
    ticker = '2928-S'
    url = "http://k-db.com/stocks/{0}?download=csv".format(ticker)
    file_name = "{0}.csv".format(ticker)
    urllib.request.urlretrieve(url, file_name)

if __name__ == '__main__':
    main()

"""
Google Finance API
"""
from datetime import datetime, timedelta
import requests
import pandas as pd

def main():
    """
    main
    """
    url = 'https://www.google.com/finance/getprices'
    code = 2928
    last_date = datetime.now()
    interval = 86400
    market = 'TYO'
    period = '1Y'

    params = {
        'q': code,
        'i': interval,
        'x': market,
        'p': period,
        'ts': last_date.timestamp()
    }

    resuest = requests.get(url, params=params)

    lines = resuest.text.splitlines()
    columns = lines[4].split('=')[1].split(',')
    pridces = lines[8:]

    first_cols = pridces[0].split(',')
    first_date = datetime.fromtimestamp(int(first_cols[0].lstrip('a')))
    result = [[first_date.date(), first_cols[1], first_cols[2],
               first_cols[3], first_cols[4], first_cols[5]]]

    for price in pridces[1:]:
        cols = price.split(',')
        date = first_date + timedelta(int(cols[0]))
        result.append([date.date(), cols[1], cols[2], cols[3], cols[4], cols[5]])

    dataframe = pd.DataFrame(result, columns=columns)
    dataframe.to_csv(str(code) + '.csv', index=False)

if __name__ == '__main__':
    main()

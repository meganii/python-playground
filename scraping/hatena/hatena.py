import requests
from calendar import Calendar
from bs4 import BeautifulSoup
from datetime import date, timedelta

def all_days(year, month, day):
    d = date(year, month, day)
    while d.year == year:
        yield d
        d += timedelta(days=1)

def main():
    hotentry_list = []
    alldays = [d.strftime('%Y%m%d') for d in all_days(2019, 1, 1)]

    for days in alldays:
        print(days)
        response = requests.get(f"https://b.hatena.ne.jp/hotentry/it/{days}")
        soup = BeautifulSoup(response.text, "html.parser")
        urllist = soup.select(".entrylist-contents-title a")
        for url in urllist:
            hotentry_list.append((days, url.get("href")))

    with open('url.txt', 'w') as f:
        for entry in hotentry_list:
            print(f"{entry[0]}\t{entry[1]}", file=f)

if __name__ == "__main__":
    main()

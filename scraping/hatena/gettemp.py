import requests
from calendar import Calendar
from bs4 import BeautifulSoup
from datetime import date, timedelta
import urllib.request
import urllib.parse
import json

def read():
    f = open('tmp.txt')
    content = f.readlines()
    f.close()
    return content

def main():
    content = read()
    entries = []

    for line in content:
        col = line.split('\t')
        url = urllib.parse.quote(col[1])
        response = requests.get("https://b.hatena.ne.jp/entry/jsonlite/?url=" + url)
        entries.append(response.text)
   
    json_data = {"entries": entries}
    json_file = open('tmp.json', 'w')
    json.dump(json_data, json_file)


if __name__ == "__main__":
    main()

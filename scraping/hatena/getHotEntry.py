import requests
from bs4 import BeautifulSoup
import urllib.parse
import json

def read():
    f = open('url.txt')
    content = f.readlines()
    f.close()
    return content

def main():
    content = read()
    entries = []

    for line in content:
        col = line.split('\t')
        url = urllib.parse.quote(col[1].strip())
        print(url)
        response = requests.get("https://b.hatena.ne.jp/entry/jsonlite/?url=" + url)
        entry = json.loads(response.text)
        entries.append(entry)
   
    json_data = {"entries": entries}
    json_file = open('bookmarks.json', 'w')
    json.dump(json_data, json_file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()

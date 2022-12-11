import csv
import sys
import json
import requests
import time


def read_csv():
    filename = sys.argv[1]
    print(filename)
    pfps = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            normal_url = row["author.profile_image_url"]
            print(normal_url)
            url = normal_url.replace("normal", "400x400")
            print(url)
            username = row["author.username"]
            print(username)
            pfps[username] = url

    return pfps


def download_pfps():
    pfps = read_csv()
    print(json.dumps(pfps, indent=4))
    folder = sys.argv[2]
    for username, url in pfps.items():
        resp = requests.get(url=url)
        print(resp.status_code)
        content = resp.content
        filename = f"{folder}\\{username}.jpg"
        with open(filename, 'w+b') as file:
            file.write(bytearray(content))
        time.sleep(0.1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_pfps()

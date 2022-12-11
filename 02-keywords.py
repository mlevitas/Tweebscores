import csv
import sys
keywords = ["anime", "manga", "otaku"]


def read_csv():
    filename = sys.argv[1]
    print(filename)
    outfile = sys.argv[2]
    with open(outfile, 'w', newline='', encoding='utf-8') as output:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            columns = ["id", "username", "is_otaku"]
            writer = csv.DictWriter(output, fieldnames=columns)
            writer.writeheader()
            seen = set()
            for row in reader:
                userid = row["author.id"]
                if userid not in seen:
                    seen.add(userid)
                else:
                    continue
                username = row["author.username"]
                description = row["author.description"].lower()
                is_otaku = False
                for keyword in keywords:
                    if keyword in description:
                        is_otaku = True
                        break
                writer.writerow({"id": userid, "username": username, "is_otaku": is_otaku})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv()

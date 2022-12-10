import json

import tweepy
import csv


def write_to_file(user_name, user_ids):
    output = "\n".join("{0}".format(n) for n in user_ids)

    with open(f"user_friends/{user_name}", 'w') as of:
        of.write(output)


def get_with_client(client, user_name):
    user_id = client.get_user(username=user_name)
    user_id = user_id.data.id
    try:
        result = client.get_users_following(id=user_id)
    except Exception as e:
        print(f"{e}")
        return False
    ids = []
    for item in result.data:
        ids.append(item.id)
    write_to_file(user_name, ids)
    return True


def get_with_api(api, user_name):
    users = api.get_friend_ids(screen_name=user_name)
    write_to_file(user_name, users)


def get_from_twitter(tweepy_api, tweepy_client):
    with open("csvs/ids.csv", 'r') as ids:
        reader = csv.reader(ids)
        for row in reader:
            user_name = row[1]
            print(f"Trying to get {user_name}")
            try:
                got_with_client = get_with_client(tweepy_client, user_name)
                if not got_with_client:
                    get_with_api(tweepy_api, user_name)
            except Exception as e:
                with open(f"user_friends/{user_name}", 'w') as of:
                    of.write("Exception")
                print(f"For user name {user_name} exception {e} occurred. Continuing")


def setup_and_query():
    keys = json.load(open("keys.json"))
    # prof keys (uses v1.1)
    auth = tweepy.OAuth1UserHandler(consumer_key=keys["API1"]["consumer_key"],
                                    consumer_secret=keys["API1"]["consumer_secret"])
    tweepy_api = tweepy.API(auth, wait_on_rate_limit=True)

    # waifu hunt project (uses v2)
    bearer_token = keys["API2"]["bearer_token"]
    tweepy_client = tweepy.Client(bearer_token=bearer_token)

    get_from_twitter(tweepy_api, tweepy_client)


if __name__ == "__main__":
    setup_and_query()

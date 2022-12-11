import tweepy
import csv
import json

keys = json.load(open("keys.json"))
bearer_token = keys["API2"]["bearer_token"]

tweepy_client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)


# Get the ids for "elites" from usernames (because API returns ids for friends/following list)
def get_elites_user_ids(input_filename, output_filename):
    with open(input_filename, 'r') as ids:
        with open(output_filename, 'w') as out:
            reader = csv.reader(ids)
            for row in reader:
                user_name = row[0]
                score = row[1]
                try:
                    user = tweepy_client.get_user(username=user_name)
                    user_id = user.data.id
                    print(f"{user_name} with {score} {user_id}")
                    out.write(f"{user_name},{user_id},{score}\n")
                except Exception as e:
                    print(f"{e}")
                continue


# We have 2 files to get IDs for:
# `compiled` is manually "cleaned" files (removed duplicate rows and all columns except username and party affiliation,
#   and then use regex to replace party affiliation with scores)
# `phi` already has scores, so just removed duplicate rows and all columns except username and scores
get_elites_user_ids("raw_tweetscores/cleaned/final/compiled.csv", "raw_tweetscores/compiled_with_ids.csv")
get_elites_user_ids("raw_tweetscores/cleaned/phi_ideal_points_cleaned.csv", "raw_tweetscores/cleaned/phi_with_ids.csv")
